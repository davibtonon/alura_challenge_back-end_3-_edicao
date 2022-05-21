from django.urls import path
from usuarios.views import login, cadastro, lista_usuarios


urlpatterns = [

    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('lista_usuarios', lista_usuarios, name='lista_usuarios'),
    # path('logout', views.logout_usuario, name='logout_usuario'),
    # path('usuarios/edita/<int:usuario_id>', views.edita_usuario, name='edita_usuario'),
    # path('usuarios/deleta/<int:usuario_id>', views.deleta_usuario, name='deleta_usuario'),
    # path('usuarios/atualiza', views.atualiza_usuario, name='atualiza_usuario'),
    
]