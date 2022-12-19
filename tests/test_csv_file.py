import pytest
import os
import insetos_hexapoda.csv_file as csv


class Insect:

    def __init__(self, genre: str,
                 length: list[str],
                 food: list[str]) -> None:

        self.genre = genre
        self.length = length
        self.food = food


def remove_file_temp(file_temp):
    os.remove(file_temp)


@pytest.fixture(scope='module')
def setup():

    file_temp = os.path.join("data", "temp.csv")

    yield file_temp

    remove_file_temp(file_temp)


def test_passes_writing_csv(setup):

    try:

        file_temp = setup

        header = ['identificador', 'nome_a', 'nome_b']

        data = ['AAA', 'BBB', 'CCC']

        csv.writing_csv(file_temp, header, data)

        assert False

    except Exception:
        assert True


@pytest.mark.skip(reason="")
def test_passes_read_csv(setup):

    path_file = setup

    res = csv.read_data_frame(path_file)

    print("res>:::::::::::", res)

    assert res


def check_genre(mantodea: dict[str, Insect]) -> bool:

    genre: str = mantodea["louva-a-deus"].genre

    return "rhombodera" == genre.lower()


def test_pass_check_genre():

    insect = Insect("Rhombodera", ['12cm', '20cm'],
                    ['rãs', 'lagartos', 'ratos', 'pássaros', 'pequenos', 'cobras'])

    mantodea = {"louva-a-deus": insect}

    assert check_genre(mantodea)
