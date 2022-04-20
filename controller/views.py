from django.shortcuts import render
from controller.form import FormFileUpload
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
           
            return render(request, 'index.html', {'form': form})
        else:
            print('Arquivo Invalido')
            print(form.errors.as_data())
            print(form.non_field_errors())
            return render(request, 'index.html', {'form': form})


