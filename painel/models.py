#!/usr/bin/python
# coding: utf-8
from django.db import models
from django.conf import settings


class Status(models.Model):
    STATUS = [
        ['created', 'Aguardando início'],
        ['structured', 'Estrutura criada'],
        ['development', 'Em desenvolvimento'],
        ['staging', 'Staging'],
        ['maturation', 'Em Maturação'],
        ['maintenance', 'Em Manutenção'],
        ['delivered', 'Entregue'],
    ]
    name = models.CharField(max_length=64, choices=STATUS)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    team = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                  through='ProjectPerson')
    status = models.ForeignKey(Status)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_model = models.BooleanField(default=False)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.name


class Device(object):
    name = models.CharField(max_length=200)
    python_command_line = models.CharField(max_length=400)
    status = models.ForeignKey(Status)


class Sensor(Device, models.Model):
    pass


class Action(Device, models.Model):
    pass


class ProjectPerson(models.Model):
    ROLES = [
        ['leader', 'Líder'],
        ['customer', 'Cliente'],
        ['developer', 'Desenvolvedor'],
        ]
    project = models.ForeignKey(Project)
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.CharField(max_length=64, choices=ROLES)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        # TODO Usar o first_name e o last_name, apenas se os dois estiverem
        # vazios/nulos usar o username
        return self.person.username + " em " + self.project.nome
