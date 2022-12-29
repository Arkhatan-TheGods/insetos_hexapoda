import csv
import os
import pickle
from datetime import datetime, time, timedelta

caminho_arquivo = os.chdir("data")

# abrindo arquivo, lendo os dados, passando para lista.
with open('Time_Tracking.csv', encoding='utf-8') as arquivo:
    lendo_dados = csv.reader(arquivo)
    dados = list(lendo_dados)
    #print(dados)


"""dados =[['date', 'Start Time', 'Lunch Start', 'Lunch End', 'End Time', 'user ID'],
['24/08/2022', '08:25', '12:15', '12:50', '19:20', '452'],
['15/07/2022', '07:35', '12:00', '', '17:55', '485'],
['03/08/2022', '07:45', '11:40', '12:33', '17:55', '155'],
['15/06/2022', '', '', '12:48', '18:20', '854'],
['20/07/2022', '09:10', '12:13', '13:00', '17:35', '54'],
['07/06/2022', '08:45', '12:25', '13:20', '', '201'],
['08/08/2022', '', '12:10', '13:00', '18:05', '120'],
['17/08/2022', '08:15', '', '', '18:02', '325'], 
['07/09/2022', '10:00', '12:10', '13:05', '', '424'],
['18/05/2022', '09:15', '12:02', '', '18:25', '211'],
['05/09/2022', '08:25', '12:05', '14:50', '18:28', '187'],
['11/11/2022', '06:24', '11:35', '12:22', '17:14', '875'],
['30/09/2022', '07:17', '11:25', '12:30', '18:03', '785'],
['16/05/2022', '11:22', '14:18', '15:22', '20:50', '124'],
['05/10/2022', '09:02', '', '13:05', '18:15', '35']]"""


nova_lista = []
horas_resultado = []

for c in dados[1:]:
    dicio = {'data:': c[0],
             'entrada trabalho:': c[1],
             'entrada almoço:': c[2],
             'saida almoço:': c[3],
             'saida trabalho:': c[4],
             'user id:': c[5], }
    nova_lista.append(dicio)
    for k, v in dicio.items():
        if v == "":
            dicio[k] = "sem dado"

for v in nova_lista:
    dt_formato = '%d/%m/%Y%H:%M'
    if v['entrada trabalho:'] not in 'sem dado' and v['saida trabalho:'] not in 'sem dado':
        entrada = v['data:'] + v['entrada trabalho:']
        entrada_dt = datetime.strptime(entrada, dt_formato)
        saida = v['data:'] + v['saida trabalho:']
        saida_dt = datetime.strptime(saida, dt_formato)
        conta = saida_dt - entrada_dt
        dicio = {'tempo trabalhado:':str(conta),'user id:':v['user id:']}
        horas_resultado.append(dicio)

    if v['entrada almoço:'] not in 'sem dado' and v['saida almoço:'] not in 'sem dado':
        entrada = v['data:'] + v['entrada almoço:']
        entrada_dt = datetime.strptime(entrada, dt_formato)
        saida = v['data:'] + v['saida almoço:']
        saida_dt = datetime.strptime(saida, dt_formato)
        conta = saida_dt - entrada_dt
        dicio.update({'tempo no almoço:':str(conta)})
        #horas_resultado.append(dicio)
    
    elif v['entrada almoço:'] in 'sem dado':
        dicio.update({'tempo no almoço:':'sem dado'})
        
    elif v['saida almoço:'] in 'sem dado':
        dicio.update({'tempo no almoço:':'sem dado'})

for c in horas_resultado:
    print('O ID: {} trabalhou {} horas e gastou com almoço: {} horas/minutos.'.format(c['user id:'],c['tempo trabalhado:'],c['tempo no almoço:']))
   
    