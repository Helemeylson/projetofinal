from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'marketplace/index.html')

def autentica_membro(request):
    return render(request,'marketplace/sou_membro.html')

def tecnologias(request):
    return render(request, "marketplace/tecnologias.html")

def tecnologia_python(request):
    return render(request, "marketplace/python.html")

def mostra_generos(request):
    dados ={ 
        1:{"nome":"Visual Novel"},
        2:{"nome":"Plataforma"},
        3:{"nome":"acao"},

      
    }
    return render(request,'marketplace/sou_membro.html', {"cards":dados})


# Create your views here.
