import os
import csv
import pytest
from datetime import datetime, timedelta
from dotenv import dotenv_values

config = dotenv_values(".env_proto")


class Timetracking:

    def __init__(self,
                 date: str,
                 start_time: str,
                 lunch_start: str,
                 lunch_end: str,
                 end_time: str,
                 user_id: str) -> None:

        self.start_time = f"{date} {start_time}" if start_time else ""
        self.lunch_start = f"{date} {lunch_start}" if lunch_start else ""
        self.lunch_end = f"{date} {lunch_end}" if lunch_end else ""
        self.end_time = f"{date} {end_time}" if end_time else ""
        self.user_id = user_id


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

        list_time_tracking: list[Timetracking] = []

        for row in csvreader:

            list_time_tracking.append(Timetracking(date=row[0],
                                                   start_time=row[1],
                                                   lunch_start=row[2],
                                                   lunch_end=row[3],
                                                   end_time=row[4],
                                                   user_id=row[5]))

    yield list_time_tracking


def test_pass_request_content(setup: list[Timetracking]) -> None:

    assert setup != []


def test_pass_csv_parse(setup) -> None:

    list_time_tracking: list[Timetracking] = setup

    tracking = []

    for time_tracking in list_time_tracking:

        notifiers = check_time(time_tracking)

        tracking.append({time_tracking.user_id.rjust(3, '0'):
                        [notifiers, None if notifiers else str(get_total_hours(time_tracking))]})

    assert tracking != []

    print()
    for key in tracking:
        print(f"{key}")
