from django.shortcuts import render
from controller.form import FormFileUpload
from django.core.files.uploadedfile import UploadedFile


# Create your views here.

def index(request):

    if request.method == 'POST':
        form = FormFileUpload(request.POST)
       
        file = request.FILES['arquivo']
        size = file.size/1048576
      
        print('Nome:', file.name)
        print('Tamanho (MB): {:.2f}'.format( size))
    else:
        form = FormFileUpload()

    return render(request, 'index.html', {'form': form})
