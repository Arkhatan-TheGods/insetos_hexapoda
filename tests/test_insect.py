import pytest

class Insect:

    def __init__(self, genre: str,
                 length: list[str],
                 food: list[str]) -> None:

        self.genre = genre
        self.length = length
        self.food = food


def check_genre(mantodea: dict[str, Insect]) -> bool:

    genre: str = mantodea["louva-a-deus"].genre

    return "rhombodera" == genre.lower()


@pytest.fixture(scope='function')
def setup():
    insect = Insect("Rhombodera", ['12cm', '20cm'],
                    ['rãs', 'lagartos', 'ratos', 'pássaros', 'pequenos', 'cobras'])

    return insect


def test_pass_check_genre(setup):

    insect = setup

    mantodea = {"louva-a-deus": insect}

    assert check_genre(mantodea)
