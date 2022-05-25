from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect

@login_required
def deleta_usuario(request, usuario_id):
    """Deleta um usuario do banco de dados"""

    user = User.objects.get(pk=usuario_id)
    user.is_active = False
    user.save()
    return redirect('lista_usuarios')
