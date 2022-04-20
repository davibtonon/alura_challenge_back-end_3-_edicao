from django.contrib import admin
from controller.models import Transacao


# Register your models here.
class ListandoTransacoes(admin.ModelAdmin):
    list_display = [
        'banco_origem', 'agencia_origem', 'conta_origem',
        'banco_destino',
        'agencia_destino',
        'conta_destino',
        'valor_transacao',
        'data']

admin.site.register(Transacao, ListandoTransacoes)