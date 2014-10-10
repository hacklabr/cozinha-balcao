from django.conf.urls import patterns, url

from painel import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.CreateProject, name='create_project'),
)
