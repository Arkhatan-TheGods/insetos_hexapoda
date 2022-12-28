from typing import Type, Mapping, List, Dict, Tuple, Any
from datetime import datetime


class ProductError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def mock_products() -> List[Any]:

    return [[1, 'Tênis Ultimate TKYX', 150.50, True],
            [2, 'Tênis BRBRBR-AAA', 360.50, True],
            [3, 'Tênis BRBRBR-PNB', 145.90, False],
            [4, 'Tênis SSSS-T', 220.50, False],
            [5, 'Tênis XV-123', 175.90, False]]


def available_search_product(products: List[Any], id: int) -> Mapping[int, list[Any]]:
    '''
    Pesquisa produto disponível
    
    Função de pesquisa para produto com status ativo

    Args
    ----
    products : List[Any] 
        Lista de produtos ativos e inativos
    id : int
        Código de produto

    Returns
    -------
    Mapping[int, list[Any]]
            Retorna um produto ativo 
    '''

    product = {}

    for element in products:
        if element[0] == id and element[0] == True:
            product = {element[0]: [element[2], element[1]]}
            break

    return product


def main():

    product_id = 2

    produto = available_search_product(mock_products(), product_id)

    if not produto:
        raise ProductError(
            {"message": ["Produto indisponível", datetime.now().timestamp()]})
    else:
        print(produto)


if __name__ == "__main__":
    try:
        main()
    except ProductError as e:
        print(e)
