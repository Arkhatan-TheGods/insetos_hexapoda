import csv
import os
from datetime import datetime, time, timedelta

caminho_arquivo = os.chdir("data\\")

# abrindo arquivo, lendo os dados, passando para lista.
with open('Time_Tracking.csv', encoding='utf-8') as arquivo:
    lendo_dados = csv.reader(arquivo)
    dados = list(lendo_dados)
    print(dados)

for pos, valor in enumerate(dados[1:]):
    if valor[1] in '':
        print(f'O ID: {valor[5]:3} não registrou entrada no serviço')
    if valor[2] in '':
        print(f'O ID: {valor[5]:3} não registrou entrada no almoço')
    elif valor[3] in '':
        print(f'O ID: {valor[5]:3} não registrou saída do almoço')
    if valor[4] in '':
        print(f'O ID: {valor[5]:3} não informa saída do trabalho')
    if valor[1] not in '' and valor[4] not in '':
        entrada = datetime.strptime(valor[1], '%H:%M')
        saida = datetime.strptime(valor[4], '%H:%M')
        calculo = saida - entrada
        if calculo < timedelta(days=0):
            calculo += timedelta(days=1)
        if valor[2] in '' or valor[3] in '':
            calculo -= timedelta(hours=1)
        if valor[2] in '' and valor[3] in '':
            calculo += timedelta(hours=1)
        print(f'O ID: {valor[5]:3} trabalhou ao total: {str(calculo)}')
