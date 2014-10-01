from django.views.generic import ListView

class IndexView(ListView):
    template_name = 'painel/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        projects = ["Projeto 1", "Projeto 2"]

        return projects