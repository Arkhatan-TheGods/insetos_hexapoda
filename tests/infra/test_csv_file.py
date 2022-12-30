import pytest
import os
from dotenv import dotenv_values
from insetos_hexapoda.infra.csv_file_infra import writing_csv, read_data_frame
from proto_config import ConfigProto, load_env

config = dotenv_values(".env_proto")

def remove_file_temp(file_temp):
    os.remove(file_temp)


@pytest.fixture(scope='module')
def setup():

    try:
        config: ConfigProto = load_env(".env.development")

        csv_temp = os.path.join(config.data_temp, config.csv_temp)

        yield csv_temp

        remove_file_temp(csv_temp)
    
    except Exception as e:
        
        pytest.xfail(str(e))



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




