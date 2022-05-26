from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from controller.models import ImportacaoRealizada

@login_required
def importacoes_realizadas(request):
    """Exibir todas as importações realizadas"""

    importacoes = ImportacaoRealizada.objects.all()
    return render(
        request, 
        'importacoes_realizadas.html', 
        {'importacoes_realizadas':importacoes})
