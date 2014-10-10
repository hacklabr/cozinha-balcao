from django.contrib import admin
from painel.models import ProjectPerson
from painel.models import Project
from painel.models import Status
from painel.models import Action
from painel.models import Sensor

admin.site.register(Project)
admin.site.register(ProjectPerson)
admin.site.register(Status)
admin.site.register(Action)
admin.site.register(Sensor)
