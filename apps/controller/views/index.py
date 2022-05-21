from django.contrib.auth.decorators import login_required
from controller.form import FormFileUpload
from apps.transacoes.transacoes import importa_arquivo_e_salva_transacoes
from django.shortcuts import redirect, render


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