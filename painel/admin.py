from django.contrib import admin
from painel.models import ProjetoPessoa
from painel.models import Projeto
from painel.models import Status
from painel.models import Acao
from painel.models import Sensor

admin.site.register(ProjetoPessoa)
admin.site.register(Projeto)
admin.site.register(Status)
admin.site.register(Acao)
admin.site.register(Sensor)