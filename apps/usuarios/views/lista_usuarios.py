from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required
def lista_usuarios(request):
    """Exibir todos os usuarios cadastros no sistema"""
    usuario_email = request.user.email
    usuarios = User.objects.all().exclude(
        email='admin@email.com.br').exclude(
        email=usuario_email).exclude(is_active=False)
    
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})