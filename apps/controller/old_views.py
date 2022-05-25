from django.shortcuts import render, redirect
from controller.form import FormFileUpload
from controller.models import ImportacaoRealizada, Transacao
from apps.transacoes.transacoes import importa_arquivo_e_salva_transacoes, procura_agencias_suspeitas, procura_contas_suspeitas, procura_transacoes_suspeitas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




# Create your views here.


# PARA UM USUARIO USAR AS FUNÇÕES ABAIXO, ELE PRECISA ESTÁ LOGADO NO SISTEMA


@login_required
def importacoes_realizadas(request):
    """Exibir todas as importações realizadas"""

    importacoes = ImportacaoRealizada.objects.all()
    return render(
        request, 
        'importacoes_realizadas.html', 
        {'importacoes_realizadas':importacoes})





def transacoes_importadas(request, importacao_id):
    """Exibir todas a importações realizadas no dia selecionado"""

    importacao = ImportacaoRealizada.objects.get(id=importacao_id)
    print(importacao.data_transacao)
    transacoes = Transacao.objects.filter(data__date=importacao.data_transacao)
    contexto = {
        'importacao': importacao,
        'transacoes': transacoes
    }
    print(importacao_id)
    return render(request, 'transacoes_importadas.html', contexto )

@login_required
def analise_transacao(request):
    """Relatorio para analise de transações realizadas no mês"""
    
    if request.method == 'POST':
        mes_procura = request.POST['mes_procura']
        mes_procura = int(mes_procura[5:])
        transacoes_suspeitas = procura_transacoes_suspeitas(mes_procura)
        agencias_suspeitas = [
            procura_agencias_suspeitas(mes_procura, 'destino'),
            procura_agencias_suspeitas(mes_procura)
            ]
        contas_suspeitas = [
            procura_contas_suspeitas(mes_procura),
            procura_contas_suspeitas(mes_procura,'origem')]
        
        contexto = {
            'transacoes_suspeitas': transacoes_suspeitas,   
            'agencias_suspeitas':agencias_suspeitas,
            'contas_suspeitas': contas_suspeitas
        }
      
        return render(request, 'analise_transacao.html', contexto)

    return render(request, 'analise_transacao.html')