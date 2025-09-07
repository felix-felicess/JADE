from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('', views.detalhe_tarefa, name='detalhe'),
]
