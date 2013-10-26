#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages

from desafioprogramacao.compra.forms import UploadArquivoForm
from desafioprogramacao.compra.models import (Arquivo, Comprador, Comerciante,
    Item, Compra)

def _calcula_receita(compras):
    """
    Método auxiliar para calcular a receita total.
    """
    receita = 0
    for compra in compras:
        receita += compra.quantidade * compra.item.preco_item
    return receita

def _grava_objetos(arquivo):
    """
    Método auxiliar para gravar todos os objetos.
    """
    arquivo_leitura = arquivo.read()
    linhas = arquivo_leitura.split('\n')
    eh_primeira_linha = True
    #remove última posição da lista
    linhas.pop()
    #lista de compras auxiliar
    compras = []
    for linha in linhas:
        if eh_primeira_linha:
            eh_primeira_linha = False
            continue
        split_linha = linha.split('\t')
        #Cria o comprador
        comprador =\
            Comprador.objects.create(nome_comprador=split_linha[0])
        #Cria o comerciante
        comerciante = Comerciante.objects.create(
            nome_comerciante=split_linha[5], endereco=split_linha[4])
        #Cria o item
        item = Item.objects.create(
            descricao_item=split_linha[1],
            preco_item=round(float(split_linha[2])))
        #Cria a compra
        compras.append((Compra.objects.create(
            quantidade=int(split_linha[3]),
            comprador=comprador,
            comerciante=comerciante,
            item=item)))
    return compras

def upload(request):
    """
    Método de view para o upload do arquivo.
    """

    if request.method == 'POST':
        form = UploadArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            compras = _grava_objetos(request.FILES.items()[0][1].file)
            receita = _calcula_receita(compras)
            #Cria o objeto arquivo
            Arquivo.objects.create(arquivo=request.FILES.items()[0][1])
            mensagem = u'Formulário enviado com sucesso.'
            messages.success(request, mensagem)
            return render_to_response(
                u'upload.html',
                {'form': UploadArquivoForm(),
                 'receita': receita},
                context_instance=RequestContext(request),
            )
        else:
            mensagem = u'Ocorreu algum erro no preenchimento do formulário.'
            mensagem += u' Verifique e envie novamente.'
            messages.error(request, mensagem)
    else:
        form = UploadArquivoForm(request.GET or None)

    return render_to_response(
        u'upload.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

