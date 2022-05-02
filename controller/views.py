from django.shortcuts import render, redirect
from controller.form import FormFileUpload
from controller.models import ImportacaoRealizada
from controller.transacoes import importa_arquivo_e_salva_transacoes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from random import randint

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).filter():
            username = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(
                request,
                username=username,
                password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('lista_usuarios')

    return render(request, 'login.html')

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
        return redirect('cadastro')
    else:  
        return render(request, 'cadastros.html')


# PARA UM USUARIO USAR AS FUNÇÕES ABAIXO, ELE PRECISA ESTÁ LOGADO NO SISTEMA
@login_required
def index(request):
    """Função para importação dos arquivos CSV."""

    if request.method == 'POST':
        form = FormFileUpload(request.POST, request.FILES)
        if form.is_valid():
            print('Arquivo valido')
            file = request.FILES['arquivo']
            #Ler o arquivo e carrega no banco de dados
            importa_arquivo_e_salva_transacoes(file, form)
            if not form.has_error('arquivo'):
                return redirect('transacoes_importadas')
        else:
            print('Arquivo Invalido')
    else:
        form = FormFileUpload()

    return render(request, 'index.html', {'form': form})

@login_required
def transacoes_importadas(request):
    """Exibir todas as importações realizadas"""

    transacoes = ImportacaoRealizada.objects.all()
    return render(
        request, 
        'transacoes_importadas.html', 
        {'transacoes_importadas':transacoes})

@login_required
def lista_usuarios(request):
    """Exibir todos os usuarios cadastros no sistema"""
    
    usuarios = User.objects.all().exclude(email='admin@email.com.br')
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def edita_usuario(request, usuario_id):
    """Editar um usuario """

    user = User.objects.get(pk=usuario_id)
   
    return render(request, 'edita_usuario.html', {'usuario': user})

@login_required
def deleta_usuario(request, usuario_id):
    """Deleta um usuario do banco de dados"""

    User.objects.filter(pk=usuario_id).delete()
    return redirect('lista_usuarios')

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

@login_required
def logout_usuario(request):
    """Desconecta uma usuario"""

    auth.logout(request)
    return redirect('login')