from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('membro/', views.autentica_membro, name='membro'),
    path('mostra/', views.mostra_generos, name='mostra'),
  
    path("tecnologias/", views.tecnologias, name="tecnologias"),
    path("tecnologias/python/", views.tecnologia_python, name="tecnologia_python"),


]