# URLs exclusivas do app Marketplace
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('membro/', views.mostra_generos, name='membro'),
    path('tecnologias/', views.tecnologias, name='tecnologias')
]
