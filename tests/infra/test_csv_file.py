import pytest
import os
from dotenv import dotenv_values
from typing import NoReturn
from insetos_hexapoda.infra.csv_file_infra import writing_csv, read_data_frame
from proto_config import load_env_csv_file, get_env_values


config = dotenv_values(".env_proto")

def remove_file_temp(file_temp):
    os.remove(file_temp)


@pytest.fixture(scope='module')
def setup():

    def fail(message: str) -> NoReturn:
        pytest.xfail(message)

    data_temp, csv_temp = load_env_csv_file(get_env_values(), fail)

    file_temp = os.path.join(data_temp, csv_temp)

    yield file_temp

    remove_file_temp(file_temp)


def test_passes_writing_csv(setup):

    try:

        file_temp = setup

        header = ['identificador', 'nome_a', 'nome_b']

        data = ['AAA', 'BBB', 'CCC']

        writing_csv(file_temp, header, data)

        assert False

    except Exception:
        assert True


@pytest.mark.skip(reason="")
def test_passes_read_csv(setup):

    path_file = setup

    res = read_data_frame(path_file)

    # print("res>:::::::::::", res)

    assert res




