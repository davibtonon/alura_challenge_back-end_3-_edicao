from django.shortcuts import render, redirect
from controller.form import FormFileUpload
from controller.models import ImportacaoRealizada, Transacao
from controller.transacoes import importa_arquivo_e_salva_transacoes, procura_agencias_suspeitas
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
        user = request.user
        if form.is_valid():
            print('Arquivo valido')
            file = request.FILES['arquivo']
            #Ler o arquivo e carrega no banco de dados
            importa_arquivo_e_salva_transacoes(file, form, user)
            if not form.has_error('arquivo'):
                return redirect('importacoes_realizadas')
        else:
            print('Arquivo Invalido')
    else:
        form = FormFileUpload()

    return render(request, 'index.html', {'form': form})

@login_required
def importacoes_realizadas(request):
    """Exibir todas as importações realizadas"""

    importacoes = ImportacaoRealizada.objects.all()
    return render(
        request, 
        'importacoes_realizadas.html', 
        {'importacoes_realizadas':importacoes})

@login_required
def lista_usuarios(request):
    """Exibir todos os usuarios cadastros no sistema"""
    usuario_email = request.user.email
    usuarios = User.objects.all().exclude(
        email='admin@email.com.br').exclude(
        email=usuario_email).exclude(is_active=False)
    
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def edita_usuario(request, usuario_id):
    """Editar um usuario """

    user = User.objects.get(pk=usuario_id)
   
    return render(request, 'edita_usuario.html', {'usuario': user})

@login_required
def deleta_usuario(request, usuario_id):
    """Deleta um usuario do banco de dados"""

    user = User.objects.get(pk=usuario_id)
    user.is_active = False
    user.save()
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

def transacoes_importadas(request, importacao_id):

 
    importacao = ImportacaoRealizada.objects.get(id=importacao_id)
    print(importacao.data_transacao)
    transacoes = Transacao.objects.filter(data__date=importacao.data_transacao)
    contexto = {
        'importacao': importacao,
        'transacoes': transacoes
    }
    print(importacao_id)
    return render(request, 'transacoes_importadas.html', contexto )

def analise_transacao(request):
    if request.method == 'POST':
        mes_procura = request.POST['mes_procura']
        mes_procura = int(mes_procura[5:])
        valor_transacao_suspeita = 18000
        valor_agencia_suspeita = 10000
        agencias = procura_agencias_suspeitas(mes_procura)
        transacoes = Transacao.objects.filter(
            data__month=mes_procura,
            valor_transacao__gte = valor_transacao_suspeita)
        contexto = {
            'transacoes': transacoes,   
            'agencias':agencias
        }
      
        return render(request, 'analise_transacao.html', contexto)

    return render(request, 'analise_transacao.html')