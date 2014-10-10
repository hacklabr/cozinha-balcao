# coding: utf-8

from django.views.generic import ListView
from django.views.generic import View
from painel.models import Project


class IndexView(ListView):
    template_name = 'painel/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        projects = Project.objects.all()

        return projects


class CreateProject(View):
    pass
