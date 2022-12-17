import pytest
import os
import insetos_hexapoda.csv_file as csv

def remove_file_temp(filte_temp):
    os.remove(filte_temp)


@pytest.fixture(scope='module')
def setup():
    
    file_temp = os.path.join("data", "temp.csv")

    yield file_temp
    
    remove_file_temp(file_temp)
    

def test_passes_writing_csv(setup):

    try:

        data = ['identificador', 'nome_a', 'nome_b']

        file_temp = setup

        csv.writing_csv(file_temp, data)

        assert True

    except Exception:
        assert False

# @pytest.mark.skip(reason="")
def test_passes_read_csv():

    path_file = ""

    res = csv.read_data_frame(path_file)

    assert res
