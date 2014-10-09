#!/usr/bin/python
# coding: utf-8
from django.db import models
from django.conf import settings

class Projeto(models.Model):
    nome=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    cliente_nome=models.CharField(max_length=200)
    equipe=models.ManyToManyField(settings.AUTH_USER_MODEL, through='ProjetoPessoa')
    created=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    e_modelo=models.BooleanField(default=False)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.nome


class Status(models.Model):
    STATUS=[
        ['aguardando_inicio', 'Aguardando início'],
        ['iniciado', 'Iniciado'],
        ['desenvolvimento', 'Desenvolvimento'],
        ['staging', 'Staging'],
        ['maturacao', 'Maturação'],
        ['manutencao', 'Manutenção'],
        ['entregue', 'Entregue'],
    ]
    nome=models.CharField(max_length=64, choices=STATUS)
    projeto=models.ForeignKey(Projeto)


class Dispositivo(object):
    nome=models.CharField(max_length=200)
    python_command_line=models.CharField(max_length=400)
    status=models.ForeignKey(Status)


class Sensor(Dispositivo, models.Model):
    pass

class Acao(Dispositivo, models.Model):
    pass

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
