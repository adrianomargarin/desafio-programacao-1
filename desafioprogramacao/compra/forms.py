#-*- coding:utf-8 -*-

from django import forms

from desafioprogramacao.compra.models import Arquivo

class UploadArquivoForm(forms.ModelForm):
    """
    Classe de formulário para upload de arquivo para ser parseado.
    """

    class Meta:
        model = Arquivo
