from datetime import datetime, timedelta
import os
import csv
import pytest
import requests
from typing import Tuple

Setup = Tuple[str, requests.models.Response]


class Timetracking:

    def __init__(self,
                 start_time: str,
                 lunch_start: str,
                 lunch_end: str,
                 end_time: str,
                 user_id: str) -> None:

        self.start_time = self.convert(start_time) if start_time != "" else None
        self.lunch_start = self.convert(lunch_start) if lunch_start != "" else None
        self.lunch_end = self.convert(lunch_end) if lunch_end != "" else None
        self.end_time = self.convert(end_time) if end_time != "" else None
        self.user_id = user_id

    def convert(self, time: str) -> datetime: \
        return datetime.strptime(time[:5], "%H:%M")

def check_time(time_tracking: Timetracking, compute_total):

    if time_tracking.start_time is None:
        return {time_tracking.user_id.rjust(3, '0'):
                [False, "start_time não registrado", None]}

    if time_tracking.lunch_start is None:
        return {time_tracking.user_id.rjust(3, '0'):
                [False, "lunch_start não registrado", None]}

    if time_tracking.lunch_end is None:
        return {time_tracking.user_id.rjust(3, '0'):
                [False, "lunch_end não registrado", None]}

    if time_tracking.end_time == None:
        return {time_tracking.user_id.rjust(3, '0'):
                [False, "end_time não registrado", None]}

    if time_tracking.start_time and time_tracking.end_time is not None:
        if time_tracking.start_time.time() > time_tracking.end_time.time():
            return {time_tracking.user_id.rjust(3, '0'):
                    [False, "Horário inconsistente para start_time", None]}

    if time_tracking.lunch_start and time_tracking.lunch_end is not None:
        if time_tracking.lunch_start.time() > time_tracking.lunch_end.time():
            return {time_tracking.user_id.rjust(3, '0'):
                    [False, "Horário inconsistente para lunch_start", None]}

    return {time_tracking.user_id.rjust(3, '0'):
            [True, None, str(compute_total(time_tracking.end_time - time_tracking.start_time,
                                            time_tracking.lunch_end - time_tracking.lunch_start))]}

def calculate_work_hours(time_work: timedelta,
                  time_lunch: timedelta) -> timedelta: return time_work - time_lunch

@pytest.fixture(scope='function')
def setup():

    CSV_URL = 'https://docs.google.com/spreadsheets/d/12IMjvF0w8MD7mYFpukNsn3F7FPJ0rlJUwM_sPnFlWW0/edit?usp=share_link'

    DRIVE_FILE_ID = CSV_URL.split('/')[-2]

    CSV_URL = f'https://docs.google.com/spreadsheets/d/{DRIVE_FILE_ID}/export?format=csv'

    response = requests.get(CSV_URL)

    file_csv_tmp = os.path.join("./data", "time_tracking_temp.csv")

    yield file_csv_tmp, response

    response.close()

    if os.path.isfile(file_csv_tmp):
        os.remove(file_csv_tmp)


def test_pass_status_code_200(setup: Setup):

    _, response = setup

    assert response.status_code == 200


def test_pass_request_content(setup: Setup):

    _, response = setup

    assert response.content


def test_pass_write_file_csv(setup: Setup):

    file_csv_tmp, response = setup

    with open(file_csv_tmp, 'wb') as csv_file:

        csv_file.write(response.content)
        csv_file.close()

    assert os.path.isfile(file_csv_tmp)

def test_pass_convert_to_datetime() -> None:

    start_time = "09:00:00"

    assert datetime.strptime(start_time[:5], "%H:%M")

def test_pass_datatime_none() -> None:

    time_tracking = Timetracking(start_time="",
                                 lunch_start="12:00:00",
                                 lunch_end="13:00:00",
                                 end_time="18:00:00",
                                 user_id="152")

    assert time_tracking.start_time is None

def test_pass_calculate_work_hours():

    time_tracking = Timetracking(start_time="08:25:00",
                                 lunch_start="12:00:00",
                                 lunch_end="13:00:00",
                                 end_time="18:00:00",
                                 user_id="152")

    if time_tracking.end_time and \
        time_tracking.start_time and \
       time_tracking.lunch_end and \
            time_tracking.lunch_start is not None:

        time_work = time_tracking.end_time - time_tracking.start_time
        time_lunch = time_tracking.lunch_end - time_tracking.lunch_start

        result = calculate_work_hours(time_work, time_lunch)
        
        # assert (datetime.strptime("08:45:00", "%H:%M:%S") - result).time() == datetime.strptime("00:00:00", "%H:%M:%S").time()
        assert str((datetime.strptime("08:35:00", "%H:%M:%S")-result).time()) == "00:00:00"
        
        # assert result.seconds == timedelta(seconds=v.timestamp())

def test_pass_csv_parse(setup: Setup):

    _, response = setup

    reader_csv = iter(csv.reader(response.content.decode(
        'utf-8').splitlines(), delimiter=','))

    next(reader_csv)

    tracking = []

    for row in reader_csv:

        time_tracking = Timetracking(start_time=row[0],
                                     lunch_start=row[1],
                                     lunch_end=row[2],
                                     end_time=row[3],
                                     user_id=row[4])

        tracking.append(check_time(time_tracking, calculate_work_hours))

    for key in tracking:
        print(f"{key}")
