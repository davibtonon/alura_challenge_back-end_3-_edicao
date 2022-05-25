from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import redirect


@login_required
def logout_usuario(request):
    """Desconecta uma usuario"""

    auth.logout(request)
    return redirect('login')