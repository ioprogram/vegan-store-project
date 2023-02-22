class Sell:
    """
    This class represent a sell transition
    """

    def __init__(self, name, quantity, buy_price, sell_price, single_revenue):
        self._name = name
        self._quantity = quantity
        self._buy_price = buy_price
        self._sell_price = sell_price
        self._single_revenue = single_revenue

    def __dict__(self):
        return {"name": self._name, "quantity": self._quantity, "buy_price": self._buy_price,
                "sell_price": self._sell_price, "single_revenue": self._single_revenue}
