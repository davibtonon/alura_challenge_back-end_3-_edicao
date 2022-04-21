from django.contrib import admin
from controller.models import Transacao, ImportacaoRealizada


# Register your models here.
class ListandoTransacoes(admin.ModelAdmin):
    list_display = [
        'banco_origem', 'agencia_origem', 'conta_origem',
        'banco_destino',
        'agencia_destino',
        'conta_destino',
        'valor_transacao',
        'data']


class ListandoImportacaoRealizada(admin.ModelAdmin):
    list_display = ['data_transacao', 'data_importacao']


admin.site.register(Transacao, ListandoTransacoes)
admin.site.register(ImportacaoRealizada, ListandoImportacaoRealizada)