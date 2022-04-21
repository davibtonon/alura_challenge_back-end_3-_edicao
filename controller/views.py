from django.shortcuts import render
from controller import transacoes
from controller.form import FormFileUpload
from controller.models import ImportacaoRealizada
from controller.transacoes import importa_arquivo_e_salva_transacoes
# Create your views here.

def index(request):
    form = FormFileUpload()
    return render(request, 'index.html', {'form': form})


def importa_transacoes(request):
    if request.method == 'POST':
        form = FormFileUpload(request.POST, request.FILES)
        if form.is_valid():
            print('Arquivo valido')
            file = request.FILES['arquivo']
            importa_arquivo_e_salva_transacoes(file, form)
            if not form.has_error('arquivo'):
                transacoes_importadas = ImportacaoRealizada.objects.all()
                return render(
                    request, 
                    'transacoes_importadas.html', 
                    {'transacoes_importadas':transacoes_importadas})

        else:
            print('Arquivo Invalido')
        
        return render(request, 'index.html', {'form': form})


