from django.db import models
# Create your models here.

class Transacao(models.Model):
    
    banco_origem = models.CharField(max_length=100)
    agencia_origem = models.CharField(max_length=15)
    conta_origem = models.CharField(max_length=7)
    banco_destino = models.CharField(max_length=100)
    agencia_destino = models.CharField(max_length=15)
    conta_destino = models.CharField(max_length=7)
    valor_transacao = models.FloatField()
    data = models.DateTimeField()

   

