# coding: utf-8

from django.views.generic import ListView

import requests

class IndexView(ListView):
    template_name = 'painel/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        projects = self.getProjectList()

        return projects

    def getProjectList(self):
        key='a0334645b2c8c9da0d96a5fd5d15e629f737818b'

        r = requests.get('http://code-devel.hacklab.com.br/projects.json?key=' + key)

        j = r.json()

        return j['projects']
