class Product:
    """
    This class represent a generic product
    """

    def __init__(self, name, quantity, sell_price=0.0, buy_price=0.0):
        self._name = name
        self._quantity = quantity
        self._sell_price = sell_price
        self._buy_price = buy_price

    def __dict__(self):
        return {"name": self._name, "quantity": self._quantity, "buy_price": self._buy_price,
                "sell_price": self._sell_price}

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def buy_price(self):
        return self._buy_price

    @property
    def sell_price(self):
        return self._sell_price
