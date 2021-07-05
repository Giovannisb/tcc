from django.db import models

# Create your models here.
class Pergunta(models.Model):
    pergunta = models.CharField(max_length=255)
    alternativa1 = models.CharField(max_length=255)
    alternativa2 = models.CharField(max_length=255)
    alternativa3 = models.CharField(max_length=255)
    alternativa4 = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)

    def __str__(self):
        return self.pergunta


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    score = models.IntegerField(default=0)