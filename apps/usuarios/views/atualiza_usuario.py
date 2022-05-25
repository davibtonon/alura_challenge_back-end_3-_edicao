from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def atualiza_usuario(request):
    """Atualiza as informações de um usuario"""

    nome = request.POST['nome']
    email = request.POST['email']
    usuario = User.objects.get(pk=request.POST['id'])
    usuario.email = email
    usuario.username= nome
    usuario.save()

    return redirect('lista_usuarios')
