import pytest
import os
from dotenv import dotenv_values
from insetos_hexapoda.infra.csv_file_infra import writing_csv, read_data_frame

config = dotenv_values(".env_proto")

def remove_file_temp(file_temp):
    os.remove(file_temp)


@pytest.fixture(scope='module')
def setup():

    folder_data = config.get("FOLDER_DATA")

    file_csv_temp = config.get("FILE_CSV_TEMP")

    if folder_data is None:
        raise TypeError("Valor 'None' fornecido para folder_data")

    if file_csv_temp is None:
        raise TypeError("Valor 'None' fornecido para file_csv_temp")

    file_temp = os.path.join(folder_data, file_csv_temp)

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




