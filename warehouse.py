from enum import Enum
from random import randint
import utils
from product import Product
import init

class ChangeProductStatus(Enum):
    SUCCESS = 1
    NOT_FOUND = 2
    NOT_ENOUGH = 3

class Warehouse:
    def __init__(self):
        self.__stock = {}
        for product in init.products:
            new_product = Product(product["name"], product["price"])
            self.__stock[new_product] = randint(1, 10)

    def change_product(self, product_name: str, quantity: int):
        cf_product_name = product_name.casefold()

        for product, stock_quantity in self.__stock.items():
            if product.name.strip().casefold() == cf_product_name:
                new_quantity = self.__stock[product] + quantity
                if new_quantity < 0:
                    return ChangeProductStatus.NOT_ENOUGH
                self.__stock[product] = new_quantity
                return ChangeProductStatus.SUCCESS

        if quantity < 0:
            return ChangeProductStatus.NOT_FOUND

        new_product_price = utils.ask_float("Enter the price of the new product: ", max_value=100, min_value=0)
        new_product = Product(product_name, new_product_price)
        self.__stock[new_product] = quantity
        return ChangeProductStatus.SUCCESS

    def get_product_stock(self, product: Product) -> int:
        return self.__stock.get(product, 0)

    def get_stock(self) -> dict:
        return dict(self.__stock)

main_warehouse = Warehouse()
