from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Transacao(models.Model):
    """Modelo de transação para salva no banco de dados"""

    banco_origem = models.CharField(max_length=100)
    agencia_origem = models.CharField(max_length=15)
    conta_origem = models.CharField(max_length=7)
    banco_destino = models.CharField(max_length=100)
    agencia_destino = models.CharField(max_length=15)
    conta_destino = models.CharField(max_length=7)
    valor_transacao = models.FloatField()
    data = models.DateTimeField()

   
class ImportacaoRealizada(models.Model):
    """ Modelo de importações realizadas para salva no banco de dados"""

    data_transacao = models.DateField()
    data_importacao = models.DateTimeField(default=timezone.now)