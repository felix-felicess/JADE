from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # senha em texto simples, ok para estudo

    def __str__(self):
        return self.nome
