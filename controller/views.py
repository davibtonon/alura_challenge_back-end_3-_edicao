from django.shortcuts import render
from controller.form import FormFileUpload
from django.core.files.uploadedfile import UploadedFile


# Create your views here.

def index(request):

    if request.method == 'POST':
        form = FormFileUpload(request.POST)
        file = request.FILES['arquivo']
        ler_arquivo(file)
    else:
        form = FormFileUpload()

    return render(request, 'index.html', {'form': form})


def ler_arquivo(file):
    """Ler um arquivo e exibir nome, tamanho e cada linha do arquivo"""

    size = file.size/1048576
    print('Nome:', file.name)
    print('Tamanho (MB): {:.2f}'.format( size))
    
    for chunk in file.chunks():
        print(chunk.decode('utf-8'))
