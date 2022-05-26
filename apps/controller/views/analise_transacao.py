from apps.transacoes.transacoes import importa_arquivo_e_salva_transacoes, procura_agencias_suspeitas, procura_contas_suspeitas, procura_transacoes_suspeitas
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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