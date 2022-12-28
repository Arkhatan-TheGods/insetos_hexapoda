
from entities.product import Product

from entities.cadat import cad_teste


def main():
    produto = Product(252, "teste", 152.45, False)

    cad_teste()

    print(produto.code)


if __name__ == "__main__":

    main()
