from django.urls import path
from usuarios.views import* 

urlpatterns = [

    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('lista_usuarios', lista_usuarios, name='lista_usuarios'),
    path('logout', logout_usuario, name='logout_usuario'),
    path('usuarios/edita/<int:usuario_id>', edita_usuario, name='edita_usuario'),
    path('usuarios/deleta/<int:usuario_id>', deleta_usuario, name='deleta_usuario'),
    path('usuarios/atualiza', atualiza_usuario, name='atualiza_usuario'),
    
]