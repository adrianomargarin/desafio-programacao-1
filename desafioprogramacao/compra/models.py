#-*- coding:utf-8 -*-

from django.db import models

class Arquivo(models.Model):
    """
    Classe que define a estrutura de dados relacionado a um arquivo.
    """
    class Meta:
        """
        Configurações de meta class.
        """
        verbose_name = u'Arquivo'
        verbose_name_plural = u'Arquivos'

    arquivo = models.FileField(
        u'Arquivo',
        upload_to='arquivos',
    )

class Comprador(models.Model):
    """
    Classe que define a estrutura de dados relacionado a um comprador.
    """

    class Meta:
        """
        Configurações de meta class.
        """
        verbose_name = u'Comprador'
        verbose_name_plural = u'Compradores'

    nome_comprador = models.CharField(
        u'Nome do comprador',
        max_length=100,
    )

    def __unicode__(self):
        return unicode(self.nome_comprador)


class Comerciante(models.Model):
    """
    Classe que define a estrutura de dados relacionado ao comerciante.
    """

    class Meta:
        """
        Configurações de meta class.
        """
        verbose_name = u'Comerciante'
        verbose_name_plural = u'Comerciantes'

    nome_comerciante = models.CharField(
        u'Nome do comerciante',
        max_length=100,
    )

    endereco = models.CharField(
        u'Endereço do comerciante',
        max_length=100,
    )

    def __unicode__(self):
        return unicode(self.nome_comerciante)


class Item(models.Model):
    """
    Classe que define a estrutura de dados relacionado a itens.
    """

    class Meta:
        """
        Configurações de meta class.
        """
        verbose_name = u'Item'
        verbose_name_plural = u'Itens'

    descricao_item = models.CharField(
        u'Descrição do item',
        max_length=100,
    )

    preco_item = models.DecimalField(
        u'Preço do item,',
        max_digits=5,
        decimal_places=2,
    )

    def __unicode__(self):
        return unicode(self.descricao_item)

class Compra(models.Model):
    """
    Classe que define a estrutura de dados relacionado a uma compra.
    """

    class Meta:
        """
        Configurações de meta class.
        """
        verbose_name = u'Compra'
        verbose_name_plural = u'Compras'

    quantidade = models.PositiveIntegerField(
        u'Quantidade a ser comprada',
    )

    comprador = models.ForeignKey(
        Comprador,
    )

    comerciante = models.ForeignKey(
        Comerciante,
    )

    item = models.ForeignKey(
        Item,
    )
