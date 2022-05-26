from django.shortcuts import render
from controller.models import ImportacaoRealizada, Transacao
from django.contrib.auth.decorators import login_required


@login_required
def transacoes_importadas(request, importacao_id):
    """Exibir todas a importações realizadas no dia selecionado"""

    importacao = ImportacaoRealizada.objects.get(id=importacao_id)
    print(importacao.data_transacao)
    transacoes = Transacao.objects.filter(data__date=importacao.data_transacao)
    contexto = { 'importacao': importacao, 'transacoes': transacoes }

    return render(request, 'transacoes_importadas.html', contexto )