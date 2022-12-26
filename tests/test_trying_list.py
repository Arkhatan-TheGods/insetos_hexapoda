from datetime import date, time, datetime, timedelta
import pytest

dados = [['Start Time', 'Lunch Start', 'Lunch End', 'End Time', 'user ID'],
         ['08:25:00',    '12:15:00',  '12:50:00', '19:20:00',     '452'],
         ['15:40:00',    '12:00:00',  '12:45:00', '17:55:00',     '485'],
         ['07:45:00',    '11:40:00',  '12:33:00', '17:55:00',     '155'],
         ['18:40:00',    '12:25:00',  '12:48:00', '18:20:00',     '854'],
         ['09:10:00',    '12:13:00',  '13:00:00', '10:25:00',     ' 54'],
         ['08:45:00',    '12:25:00',  '13:20:00', '18:10:00',     '201'],
         ['',            '12:10:00',  '13:00:00', '18:05:00',     '120'],
         ['08:15:00',            '',          '', '18:02:00',     '325'],
         ['10:00:00',    '12:10:00',  '13:05:00',         '',     '424'],
         ['09:15:00',    '12:02:00',          '', '18:25:00',     '211'],
         ['08:25:00',    '13:25:00',  '12:15:00', '18:28:00',     '187']]

for pos, valor in enumerate(dados[1:]):
    if valor[0] in '':
        print(f'O ID: {valor[4]} não registrou entrada no serviço.')
    if valor[1] in '':
        print(f'O ID: {valor[4]} não registrou entrada no almoço.')
    elif valor[2] in '':
        print(f'O ID: {valor[4]} não registrou saída do almoço.')
    if valor[3] in '':
        print(f'O ID: {valor[4]} não informa saída do trabalho.')
    if valor[0] not in '' and valor[3] not in '':
        entrada = datetime.strptime(valor[0], '%H:%M:%S')
        saida = datetime.strptime(valor[3], '%H:%M:%S')
        calculo = saida - entrada
        if calculo < timedelta(days=0):
            calculo += timedelta(days=1)
        if valor[1] in '' or valor[2] in '':
            calculo -= timedelta(hours=1)
        if valor[1] in '' and valor[2] in '':
            calculo += timedelta(hours=1)
        print(f'O ID: {valor[4]} trabalhou ao total: {calculo}.')


@pytest.fixture(scope='function')
def setup():
    lista = ['08:25:00', '12:15:00', '12:50:00', '19:20:00', '452']
    yield lista


def test_pass_lista_carregada(setup) -> None:
    lista = setup
    assert lista != []
    assert lista
    assert len(lista) > 0
    assert type(lista) == list
    assert isinstance(lista, list)


def test_pass_str_in_list(setup) -> str:
    lista = setup
    for i, e in enumerate(lista):
        assert type(
            e) == str, f'na posição {i} é esperado uma informação em formato string.'


def test_entrada_trabalho(setup):
    entrada_trabalho = setup[0]
    assert entrada_trabalho != None


def test_entrada_almoco(setup):
    entrada_almoco = setup[1]
    assert entrada_almoco != None


def test_saida_almoco(setup):
    saida_almoco = setup[2]
    assert saida_almoco != None


def test_saida_trabalho(setup):
    saida_trabalho = setup[3]
    assert saida_trabalho != None


def test_convertendo_str_datetime(setup):
    entrada = setup[0]
    entrada_dt = datetime.strptime(entrada, '%H:%M:%S')
    lunch = setup[1]
    lunch_dt = datetime.strptime(lunch, '%H:%M:%S')
    lunch_end = setup[2]
    lunch_end_dt = datetime.strptime(lunch_end, '%H:%M:%S')
    saida = setup[3]
    saida_dt = datetime.strptime(saida, '%H:%M:%S')
    assert isinstance(entrada_dt, datetime)
    assert isinstance(lunch_dt, datetime)
    assert isinstance(lunch_end_dt, datetime)
    assert isinstance(saida_dt, datetime)


def test_validando_calculo_datetime(setup):
    entrada = setup[0]
    entrada_dt = datetime.strptime(entrada, '%H:%M:%S')
    saida = setup[3]
    saida_dt = datetime.strptime(saida, '%H:%M:%S')
    calculo = saida_dt - entrada_dt

    if calculo < timedelta(days=0):
        calculo += timedelta(days=1)

    calculo_str = str(calculo)
    assert calculo_str == '10:55:00'
