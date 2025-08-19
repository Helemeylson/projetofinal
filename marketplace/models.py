from django.db import models

# Create your models here.
# vou programar o modelo aqui Classes mapeadas com tabelas
# persistencia?
#orientação a objetos
#classe ===> tabela
#lcoalhost:8080 - site
#localhost:8080/admin
#herança
class Membro(models.Model):
    email = models.CharField(max_length=50, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False)

class Genero(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
   


