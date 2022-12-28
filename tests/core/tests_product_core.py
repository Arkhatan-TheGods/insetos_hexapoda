import pytest
from insetos_hexapoda.entities.product import Product
from insetos_hexapoda.core.product_core import available_search_product
from typing import Type, Mapping, List, Dict, Tuple, Any

@pytest.fixture(scope='module')
def setup():

    mock_products = [[1, 'Tênis Ultimate TKYX', 150.50, True],
                     [2, 'Tênis BRBRBR-AAA', 360.50, True],
                     [3, 'Tênis BRBRBR-PNB', 145.90, False],
                     [4, 'Tênis SSSS-T', 220.50, False],
                     [5, 'Tênis XV-123', 175.90, False]]

    yield mock_products


@pytest.fixture(scope='module')
def setup_class():

    yield [Product(1, 'Tênis Ultimate TKYX', 150.50, True),
           Product(2, 'Tênis BRBRBR-AAA', 360.50, True),
           Product(3, 'Tênis BRBRBR-PNB', 145.90, False),
           Product(4, 'Tênis SSSS-T', 220.50, False),
           Product(5, 'Tênis XV-123', 175.90, False)]

def test_pass_product_not_available(setup) -> None:

    product_id: int = 5

    produto:Mapping[int, list[Any]] = available_search_product(setup, product_id)

    assert not produto


def test_pass_product_available(setup) -> None:

    product_id:int = 1

    produto:Mapping[int, list[Any]] = available_search_product(setup, product_id)

    assert produto

def test_pass_check_type_class_products(setup_class) -> None:

    assert isinstance(setup_class[0], Product)
