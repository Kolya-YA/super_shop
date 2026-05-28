class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price

    def __str__(self):
        return f"{self.name}:\t\t€{self.__price:04.2f}"
