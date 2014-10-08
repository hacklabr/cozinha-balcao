#!/usr/bin/python
# coding: utf-8
from django.db import models
from django.conf import settings

class Projeto(models.Model):
    STATUS=[
        ['aguardando_inicio', 'Aguardando início']
        ['desenvolvimento', 'Desenvolvimento']
        ['staging', 'Staging']
        ['maturacao', 'Maturação']
        ['manutencao', 'Manutenção']
        ['entregue', 'Entregue']
    ]
    nome=models.CharField(max_length=200)
    cliente_nome=models.CharField(max_length=200)
    equipe=models.ManyToManyField(settings.AUTH_USER_MODEL, through='ProjetoPessoa')
    created=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=64, choices=STATUS)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.nome


class ProjetoPessoa(models.Model):
    PAPEIS=[
        ['lider', 'Líder'],
        ['cliente', 'Cliente'],
        ['desenvolvedor', 'Desenvolvedor'],
        ]
    projeto=models.ForeignKey(Projeto)
    pessoa=models.ForeignKey(settings.AUTH_USER_MODEL)
    papel=models.CharField(max_length=64, choices=PAPEIS)


    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        # TODO Usar o first_name e o last_name, apenas se os dois estiverem vazios/nulos usar o username
        return self.pessoa.username + " em " + self.projeto.nome


class Acao(models.Model):
    nome=models.CharField(max_length=100)
    python_command_line=models.CharField(max_length=400)
    projeto=models.ForeignKey(Projeto)
