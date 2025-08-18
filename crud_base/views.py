from django.shortcuts import render, redirect
from django.http import HttpResponse

def criar_usuario(request):
    return render(request, 'crud_base/usuario_lead.html')


# Create your views here.
