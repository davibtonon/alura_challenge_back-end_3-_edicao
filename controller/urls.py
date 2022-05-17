from django.urls import path
from controller import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importacoes_realizadas', views.importacoes_realizadas, name='importacoes_realizadas' ),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout_usuario, name='logout_usuario'),
    path('lista_usuarios', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/edita/<int:usuario_id>', views.edita_usuario, name='edita_usuario'),
    path('usuarios/deleta/<int:usuario_id>', views.deleta_usuario, name='deleta_usuario'),
    path('usuarios/atualiza', views.atualiza_usuario, name='atualiza_usuario'),
    path('transacoes_importadas/<int:importacao_id>', views.transacoes_importadas, name='transacoes_importadas'),
    path('analise_transacao/', views.analise_transacao, name='analise_transacao'),
]
