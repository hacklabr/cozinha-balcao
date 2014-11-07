#!/usr/bin/python
# coding: utf-8
from django import settings
from django.db import models
from django.models import User


class Loggable(object):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifier = models.ForeignKey(settings.AUTH_USER_MODEL)
    last_modified = models.DateTimeField(auto_now=True)


class Status(Loggable, models.Model):
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


class ContactEntry(Loggable, models.Model):
    KINDS = [
        ['phone', 'Telefone'],
        ['email', 'Email'],
        ['skype', 'Skype'],
        ['address', 'Endereço']
        ]
    kind = models.CharField(max_length=200, choices=KINDS)
    data = models.CharField(max_length=200)


class Person(Loggable, models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    contacts = models.ManyToManyField(ContactEntry)


class Customer(Loggable, models.Model):
    name = models.CharField(max_length=200)
    team = models.ManyToManyField(Person, through='ProjectPerson')


class Project(Loggable, models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    participants = models.ManyToManyField(Person, through='ProjectPerson')
    customer_name = models.CharField(max_length=200)
    status = models.ForeignKey(Status)
    contract_start = models.DateTimeField(auto_now_add=True)
    contract_end = models.DateTimeField(auto_now_add=True)
    maturation_start = models.DateTimeField(auto_now_add=True)
    maturation_end = models.DateTimeField(auto_now_add=True)
    maintenance_start = models.DateTimeField(auto_now_add=True)
    maintenance_end = models.DateTimeField(auto_now_add=True)
    hosting_start = models.DateTimeField(auto_now_add=True)
    hosting_end = models.DateTimeField(auto_now_add=True)
    wp_version = models.CharField(max_length=5)
    is_model = models.BooleanField(default=False)

    def leader(self):
        """Returns the participant with role of 'leader'"""
        pass

    def is_maintenance_active(self):
        """If current_date >= hosting_start and current_date <= hosting_end """
        pass

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.name


class ProjectPerson(Loggable, models.Model):
    ROLES = [
        ['leader', 'Líder'],
        ['customer', 'Cliente'],
        ['developer', 'Desenvolvedor'],
        ['designer', 'Designer'],
        ]
    project = models.ForeignKey(Project)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=64, choices=ROLES)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        # TODO Usar o first_name e o last_name, apenas se os dois estiverem
        # vazios/nulos usar o username
        return self.person.username + " em " + self.project.nome


class Device(Loggable, object):
    name = models.CharField(max_length=200)
    python_command_line = models.CharField(max_length=400)
    status = models.ForeignKey(Status)


class Sensor(Device, models.Model):
    pass


class Action(Device, models.Model):
    pass
