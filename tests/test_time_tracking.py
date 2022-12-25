import os
import csv
import pytest
from datetime import datetime, timedelta
from dotenv import dotenv_values
from typing import Tuple
import httpx

config = dotenv_values(".env_proto")

class Timetracking:

    def __init__(self,
                 date: str,
                 start_time: str,
                 lunch_start: str,
                 lunch_end: str,
                 end_time: str,
                 user_id: str) -> None:

        self.start_time_is_empty = self.is_empty_string(start_time)
        self.lunch_start_is_empty = self.is_empty_string(lunch_start)
        self.lunch_end_is_empty = self.is_empty_string(lunch_end)
        self.end_time_is_empty = self.is_empty_string(end_time)

        self.start_time = self.convert(date, start_time)
        self.lunch_start = self.convert(date, lunch_start)
        self.lunch_end = self.convert(date, lunch_end)
        self.end_time = self.convert(date, end_time)
        self.user_id = user_id

    def is_empty_string(self, value: str) -> bool:
        return True if not value else False

    def convert(self, date: str, time: str) -> datetime:

        date_time = f"{date} {time[:5]}"
        
        return datetime.strptime(date_time, "%d/%m/%Y %H:%M") \
            if time else datetime.strptime("00:00", "%H:%M")

    def convert_to_date(self, date: str, format) -> datetime:
        return datetime.strptime(date, format)

def check_time(time_tracking: Timetracking):

    messages = []

    if time_tracking.start_time_is_empty:
        messages.append("start_time não registrado")

    if time_tracking.lunch_start_is_empty:
        messages.append("lunch_start não registrado")

    if time_tracking.lunch_end_is_empty:
        messages.append("lunch_end não registrado")

    if time_tracking.end_time_is_empty:
        messages.append("end_time não registrado")

    return messages

def get_total_hours(time_tracking: Timetracking) -> timedelta:

    time_work = time_tracking.end_time - time_tracking.start_time
    time_lunch = time_tracking.lunch_end - time_tracking.lunch_start

    return time_work - time_lunch


@pytest.fixture(scope='function')
def proto_setup():

    lista = [
        ["24/08/2022", "", "12:05:00", "13:08:00", "19:35:00", "201"],
        ["05/07/2022", "10:14:00", "12:22:00", "13:05:00", "20:05:00", "302"],
        ["18/10/2022", "08:25:00", "", "13:10:00", "18:55:00", "403"]
    ]

    lista_time_tracking = []

    for row in lista:
        lista_time_tracking.append(Timetracking(date=row[0],
                                                start_time=row[1],
                                                lunch_start=row[2],
                                                lunch_end=row[3],
                                                end_time=row[4],
                                                user_id=row[5]))

    yield lista_time_tracking

def test_pass_datatime_is_empty(proto_setup) -> None:

    time_tracking = proto_setup

    assert time_tracking[0].start_time_is_empty

def test_pass_calculate_work_hours(proto_setup):

    time_tracking = proto_setup

    total_hours = get_total_hours(time_tracking[1])

    assert (timedelta(hours=9, minutes=8) -
            total_hours).total_seconds() == 0.0

@pytest.fixture(scope='module')
def setup():

    folder_data = config.get("FOLDER_DATA")

    file_csv = config.get("FILE_CSV")

    if folder_data is None:
        raise TypeError("Valor 'None' fornecido para folder_data")

    if file_csv is None:
        raise TypeError("Valor 'None' fornecido para file_csv")

    file_csv = os.path.join(folder_data, file_csv)
    
    with open(file_csv) as file:
        
        csvreader = csv.reader(file)
        
        next(csvreader)

        rows = []

        for row in csvreader:
            rows.append(row)

    yield rows


def test_pass_request_content(setup: list):

    assert setup != []

def test_pass_csv_parse(setup: list):
    
    tracking = []

    for row in setup:

        time_tracking = Timetracking(date=row[0],
                                     start_time=row[1],
                                     lunch_start=row[2],
                                     lunch_end=row[3],
                                     end_time=row[4],
                                     user_id=row[5])

        notifiers = check_time(time_tracking)

        tracking.append({time_tracking.user_id.rjust(3, '0'):
                        [notifiers, None if notifiers else str(get_total_hours(time_tracking))]})

    assert tracking != []
    
    print()
    for key in tracking:
        print(f"{key}")
