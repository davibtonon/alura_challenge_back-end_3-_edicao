from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required
def edita_usuario(request, usuario_id):
    """Editar um usuario """

    user = User.objects.get(pk=usuario_id)
   
    return render(request, 'edita_usuario.html', {'usuario': user})