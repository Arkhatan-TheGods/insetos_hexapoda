class Product():

    def __init__(self, code: int,
                 description: str,
                 price: float,
                 status: bool) -> None:

        self.code = code
        self.description = description
        self.price = price
        self.status = status
