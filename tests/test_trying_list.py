
import csv
import os
import pytest
from datetime import datetime
from proto_config import ConfigProto, load_env


@pytest.fixture(scope='function')
def setup():

    try:
        config: ConfigProto = load_env(".env.development")

        file_csv = os.path.join(config.data_temp, config.csv_file)

        # abrindo arquivo, lendo os dados, passando para lista.
        with open(file_csv, encoding='utf-8') as arquivo:
            lendo_dados = csv.reader(arquivo)
            dados = list(lendo_dados)
            # print(dados)

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

        return dados

    except Exception as e:

        pytest.xfail(str(e))


def test_trying_list(setup):

    dados = setup

    nova_lista = []
    horas_resultado = []
    dicio = {}

    for c in dados[1:]:
        dicio = {'data:': c[0],
                 'entrada trabalho:': c[1],
                 'entrada almoço:': c[2],
                 'saida almoço:': c[3],
                 'saida trabalho:': c[4],
                 'user id:': c[5], }

        nova_lista.append(dicio)

    for v in nova_lista:
        dt_formato = '%d/%m/%Y%H:%M'
        if v['entrada trabalho:'] and v['saida trabalho:'] and v['entrada almoço:'] and v['saida almoço:']:
            entrada = v['data:'] + v['entrada trabalho:']
            entrada_dt = datetime.strptime(entrada, dt_formato)
            saida = v['data:'] + v['saida trabalho:']
            saida_dt = datetime.strptime(saida, dt_formato)
            conta = saida_dt - entrada_dt
            entrada2 = v['data:'] + v['entrada almoço:']
            entrada2_dt = datetime.strptime(entrada2, dt_formato)
            saida2 = v['data:'] + v['saida almoço:']
            saida2_dt = datetime.strptime(saida2, dt_formato)
            conta2 = saida2_dt - entrada2_dt
            total = conta - conta2
            dicio = {'tempo efetivo:': str(total), 'user id:': v['user id:']}
            horas_resultado.append(dicio)
    assert horas_resultado


"""
[{'tempo trabalhado:': '10:55:00', 'user id:': '452'},
 {'tempo trabalhado:': '10:10:00', 'user id:': '155'},
  {'tempo trabalhado:': '8:25:00', 'user id:': '54'}, 
  {'tempo trabalhado:': '10:03:00', 'user id:': '187'}, 
  {'tempo trabalhado:': '10:50:00', 'user id:': '875'},
   {'tempo trabalhado:': '10:46:00', 'user id:': '785'}, 
   {'tempo trabalhado:': '9:28:00', 'user id:': '124'}]
"""
