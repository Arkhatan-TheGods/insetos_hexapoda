import os
import csv
import pytest
import pickle
from datetime import datetime, timedelta
from typing import Any, NoReturn, TypedDict
from insetos_hexapoda.entities.time_tracking import Timetracking
from proto_config import load_env_time_tracking, get_env_values


def check_time(time_tracking: Timetracking):

    messages = []

    if not time_tracking.start_time:
        messages.append("start_time não registrado")

    if not time_tracking.lunch_start:
        messages.append("lunch_start não registrado")

    if not time_tracking.lunch_end:
        messages.append("lunch_end não registrado")

    if not time_tracking.end_time:
        messages.append("end_time não registrado")

    return messages


def get_total_hours(time_tracking: Timetracking) -> timedelta:

    def convert(date_time: str) -> datetime:
        return datetime.strptime(date_time[:16], "%d/%m/%Y %H:%M")

    start_time = convert(time_tracking.start_time)
    lunch_start = convert(time_tracking.lunch_start)
    lunch_end = convert(time_tracking.lunch_end)
    end_time = convert(time_tracking.end_time)

    time_work = end_time - start_time
    time_lunch = lunch_end - lunch_start

    return time_work - time_lunch


@pytest.fixture(scope='function')
def proto_setup():

    mock_csv = [
        ["24/08/2022", "", "12:05:00", "13:08:00", "19:35:00", "201"],
        ["05/07/2022", "10:14:00", "12:22:00", "13:05:00", "20:05:00", "302"],
        ["18/10/2022", "08:25:00", "", "13:10:00", "18:55:00", "403"]
    ]

    lista_time_tracking: list[Timetracking] = []

    for row in mock_csv:
        lista_time_tracking.append(Timetracking(date=row[0],
                                                start_time=row[1],
                                                lunch_start=row[2],
                                                lunch_end=row[3],
                                                end_time=row[4],
                                                user_id=row[5]))

    yield lista_time_tracking


def test_pass_datatime_is_empty(proto_setup) -> None:

    list_time_tracking: list[Timetracking] = proto_setup

    assert not list_time_tracking[0].start_time


def test_pass_calculate_work_hours(proto_setup) -> None:

    list_time_tracking: list[Timetracking] = proto_setup

    total_hours = get_total_hours(list_time_tracking[1])

    assert (timedelta(hours=9, minutes=8) -
            total_hours).total_seconds() == 0.0


@pytest.fixture(scope='module')
def setup():

    def fail(message: str) -> NoReturn:
        pytest.xfail(message)
    
    folder_data, file_csv, tracking_temp_pickle = load_env_time_tracking(get_env_values(), fail)

    file_csv = os.path.join(folder_data, file_csv)

    file_pickle = os.path.join(folder_data, tracking_temp_pickle)

    with open(file_csv) as file:

        csvreader = csv.reader(file)

        next(csvreader)

        list_time_tracking: list[Timetracking] = []

        for row in csvreader:

            list_time_tracking.append(Timetracking(date=row[0],
                                                   start_time=row[1],
                                                   lunch_start=row[2],
                                                   lunch_end=row[3],
                                                   end_time=row[4],
                                                   user_id=row[5]))

    yield list_time_tracking, file_pickle

    if os.path.isfile(file_pickle):
        os.remove(file_pickle)


def serialization_dump(file_pickle, tracking) -> None:
    with open(file_pickle, "wb") as outfile:
        pickle.dump(tracking, outfile)


def deserialization_dump(tracking) -> Any:
    with open(tracking, "rb") as infile:
        return pickle.load(infile)


def test_pass_request_content(setup: tuple[list[str], str]) -> None:

    list_time_tracking, _ = setup

    assert list_time_tracking != []


def test_pass_request_check_file_pickle(setup: tuple[list[str], str]) -> None:

    _, file_pickle = setup

    assert file_pickle


def test_pass_create_file_pickle(setup) -> None:

    _, file_pickle = setup

    serialization_dump(file_pickle, [{"452": [[], "9:35:00"]}])

    assert os.path.isfile(file_pickle)


def test_pass_deserialization_data(setup) -> None:

    _, file_pickle = setup

    tracking = [{"453": [[], "10:35:00"]}]

    serialization_dump(file_pickle, tracking)

    tracking_temp: list[dict[str, list[Any]]
                        ] = deserialization_dump(file_pickle)

    assert tracking == tracking_temp


def test_pass_csv_parse(setup) -> None:

    list_time_tracking, _ = setup

    tracking = []

    for time_tracking in list_time_tracking:

        notifiers = check_time(time_tracking)

        tracking.append({time_tracking.user_id.rjust(3, '0'):
                        [notifiers, None if notifiers else str(get_total_hours(time_tracking))]})

    assert tracking != []

    print()
    for key in tracking:
        print(f"{key}")


@pytest.fixture(scope='function')
def setup_simulado():

    def format_user_id(user_id: str) -> str:
        return user_id.ljust(3, "0")

    return iter([['Date', 'Start Time', 'Lunch Start', 'Lunch End', 'End Time', 'user ID'],
                 ['24/08/2022', '08:25:00', '12:15:00', '12:50:00', '19:20:00', '452'],
                 ['15/07/2022', '15:40:00', '12:00:00', '12:45:00', '17:55:00', '485'],
                 ['03/08/2022', '07:45:00', '12:40:00', '13:33:00', '17:55:00', '155'],
                 ['15/06/2022', '07:12:00', '12:25:00', '12:48:00', '18:20:00', '854'],
                 ['20/07/2022', '09:10:00', '12:13:00', '13:00:00', '10:25:00', '54'],
                 ['07/06/2022', '08:45:00', '12:25:00', '13:20:00', '18:10:00', '201'],
                 ['08/08/2022', '', '12:10:00', '13:00:00', '18:05:00', '120'],
                 ['17/08/2022', '08:15:00', '', '', '18:02:00', '325'],
                 ['07/09/2022', '10:00:00', '12:10:00', '13:05:00', '', '424'],
                 ['18/05/2022', '09:15:00', '12:02:00', '', '18:25:00', '211'],
                 ['05/09/2022', '08:25:00', '13:25:00', '12:15:00', '18:28:00', '187']]), format_user_id

def test_simulado(setup_simulado):
    

    dados, fn_format = setup_simulado

    next(dados)

    nova_lista = []

    falhas = []

    relatorio = []

    for element in dados:
        nova_lista.append({'data': element[0],
                           'registro_entrada': element[1],
                           'almoco_saida': element[2],
                           'almoco_retorno': element[3],
                           'registro_saida': element[4],
                           'user_id': element[5]})

    def calcula_total_hora(data: str,
                           registro_entrada: str,
                           almoco_saida: str,
                           almoco_retorno: str,
                           registro_saida: str):
        
        mascara = "%d/%m/%Y %H:%M:%S"

        hora_entrada = datetime.strptime(f"{data} {registro_entrada}", mascara)
        hora_almoco_saida = datetime.strptime(f"{data} {almoco_saida}", mascara)
        hora_almoco_retorno = datetime.strptime(f"{data} {almoco_retorno}", mascara)
        hora_saida = datetime.strptime(f"{data} {registro_saida}", mascara)
        
        horas_calculadas = ((hora_saida - hora_entrada) -
                            (hora_almoco_retorno - hora_almoco_saida))

        return str(horas_calculadas)
    
    d:TypedDict

    for d in nova_lista:
        
        falhas = []

        if not d.get('registro_entrada'):
            falhas.append("registro_entrada não identificado")

        if not d.get('almoco_saida'):
            falhas.append("almoco_saida não identificado")

        if not d.get('almoco_retorno'):
            falhas.append("almoco_retorno não identificado")

        if not d.get('registro_saida'):
            falhas.append("registro_saida não identificado")

        if falhas:
            relatorio.append(
                {fn_format(str(d.get('user_id'))): [falhas, None]})

        else:
            total_horas = calcula_total_hora(str(d.get('data')),
                                             str(d.get('registro_entrada')),
                                             str(d.get('almoco_saida')),
                                             str(d.get('almoco_retorno')),
                                             str(d.get('registro_saida')))

            relatorio.append(
                {fn_format(str(d.get('user_id'))): [[], total_horas]})

    print()
    for rel in relatorio:
        print(rel)
