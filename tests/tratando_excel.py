import pandas as pd
import os
import csv
from time import sleep

caminho_arquivo = os.chdir("tests\\")                           



#os processos a seguir define o nome do arquivo, o caminho do arquivo excel com o nome, depois faz a conversão do arquivo excel para csv
#arquivo = 'tempo.xlsx'
#excel_arquivo = pd.read_excel(arquivo)
#excel_arquivo.to_csv("tempos.csv", index = None, header=True)

with open('tempos.csv',encoding='utf-8') as dados:
    lendo = csv.reader(dados, delimiter =',')
    list_information = list(lendo)
    print(list_information)