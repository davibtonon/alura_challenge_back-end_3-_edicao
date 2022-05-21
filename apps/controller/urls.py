from django.urls import path
from controller.views import index

urlpatterns = [
    path('', index, name='index'),
    # path('importacoes_realizadas', views.importacoes_realizadas, name='importacoes_realizadas' ),
    # path('transacoes_importadas/<int:importacao_id>', views.transacoes_importadas, name='transacoes_importadas'),
    # path('analise_transacao/', views.analise_transacao, name='analise_transacao'),
]
