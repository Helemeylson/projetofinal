from django.shortcuts import render, redirect
from django.http import HttpResponse
from marketplace.models import Membro, Genero

# Create your views here.
def index(request):
    return render(request, 'marketplace/index.html')

def tecnologias(request):
    return render (request, 'marketplace/tecnologias.html')

def mostra_generos(request):
    membros = Membro.objects.all()
    generos = Genero.objects.all()

    return render(request, 'marketplace/sou_membro.html', {
    "membros": membros,
    "generos": generos })
