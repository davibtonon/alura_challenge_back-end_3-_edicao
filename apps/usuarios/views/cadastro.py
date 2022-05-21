from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from random import randint

def cadastro(request):
    """Função que cadastra novo usuarios no sistema"""
    
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = str(randint(100000, 999999))
        if User.objects.filter(email=email).filter():
            messages.error(request, 'Email já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, 
            email=email, 
            password=senha)
        user.save()

        message = f'Ola, {nome} sua senha de acesso é {senha}'
        subject = 'Cadastro realizado com sucesso'
        from_email = 'django_servidor@gmail.com'
        user.email_user(subject, message, from_email)

        messages.success(request, 'Usuario criado com sucesso')
        return redirect('index')
    else:  
        return render(request, 'cadastros.html')