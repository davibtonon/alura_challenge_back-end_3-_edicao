from controller.models import Transacao, ImportacaoRealizada
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.mail import send_mail
from django.db.models import Sum, F 

def importa_arquivo_e_salva_transacoes(file, form, user):
    """
    Salva as transacoes bancarias de um arquivo csv.
    Caso o arquivo e as transações sejam validas"""

    size = file.size/1048576
    data_inicial = None
    datas_transacoes = None
    print('Nome:', file.name)
    print('Tamanho (MB): {:.2f}'.format( size)) 

    for line in file:
        
        # Usa decode no arquivo binario e passa para texto.    
        lista_transacoes = line.decode('utf-8')
        lista_transacoes = lista_transacoes.strip()
        lista_transacoes = lista_transacoes.split(',')

        # Transformar uma string em um objeto datetime
        # Usa a função 'make_aware' para corrigi o erro no time zone
        data =  datetime.fromisoformat(lista_transacoes[7])
        data = make_aware(data)
        
        # Usado para add uma data inicial no arquivo
        if data_inicial is None:
            data_inicial = datetime.fromisoformat(lista_transacoes[7])
            data_inicial = make_aware(data_inicial)
        
        # Buscar no banco de dados todas as datas das transações
        # Talvez precise muda isso acho que não é a melhor forma.
        if datas_transacoes is None:
            datas_transacoes = Transacao.objects.dates('data', 'year')
        
        # Verificar se as transações do dia foram importadas antes.
        if data_inicial.date() in datas_transacoes:
            messagem_erro = f" Transações do dia {data_inicial.date()} já foram enviadas"
            print(messagem_erro)
            form.add_error('arquivo', messagem_erro)
            return
           
        transacao = Transacao(
                banco_origem=lista_transacoes[0],
                agencia_origem=lista_transacoes[1], 
                conta_origem=lista_transacoes[2], 
                banco_destino=lista_transacoes[3], 
                agencia_destino=lista_transacoes[4], 
                conta_destino=lista_transacoes[5], 
                valor_transacao=lista_transacoes[6],
                data=data,
                usuario=user)
        
        # Verificar se a data da primeira linha é igual a linha atual
        if data.date() == data_inicial.date():
            try:
                transacao.full_clean()
                transacao.save()
            except ValidationError as e:
                print(e.message_dict)
        else:
            print('As datas são diferentes')
             
    ImportacaoRealizada(data_transacao=data_inicial.date(), usuario=user).save()

def envia_email(nome, email, senha):
  
    message = f'Ola, {nome} sua senha de acesso é {senha}'
    subject = 'Cadastro realizado com sucesso'
    from_email = 'django_servidor@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list )

def procura_agencias_suspeitas(mes_procura, tipo:str='origem' ):

    agencia = 'agencia_' + tipo
    banco = 'banco_' + tipo
    valor_suspeito = 100
    transacoes = Transacao.objects.values(agencia, banco)\
        .annotate(valor_movimentacao_mes=Sum('valor_transacao'))\
        .filter(
            valor_movimentacao_mes__gte=valor_suspeito,
            data__month=mes_procura)
    [print(t) for t in transacoes]