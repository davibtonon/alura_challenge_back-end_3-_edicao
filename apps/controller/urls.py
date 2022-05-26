from django.urls import path
from controller.views import*

urlpatterns = [
    path('', index, name='index'),
    path('importacoes_realizadas', importacoes_realizadas, name='importacoes_realizadas' ),
    path('transacoes_importadas/<int:importacao_id>', transacoes_importadas, name='transacoes_importadas'),
    path('analise_transacao/', analise_transacao, name='analise_transacao'),
]
