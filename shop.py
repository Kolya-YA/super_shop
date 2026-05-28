from warehouse import main_warehouse, ChangeProductStatus
import utils

class Shop:
    def __init__(self, name: str):
        self.name = name.strip() or "Super shop"

    def show_current_stock(self):
        stock = main_warehouse.get_stock()
        print(f"\nCurrent stock for {self.name}:")
        utils.separator()

        if not stock:
            print("No products in stock.")
            return

        for product, quantity in stock.items():
            print(f"{product}:\t{quantity}")
        utils.separator()

    def refill_warehouse(self):
        print("\nRefilling warehouse...")
        self.show_current_stock()
        product_name = utils.ask_str("Enter the product name: ")
        product_quantity = utils.ask_int("Enter the quantity: ", 100, 1)
        result = main_warehouse.change_product(product_name.strip(), product_quantity)
        if result != ChangeProductStatus.SUCCESS:
            print("Failed to add product")
            return
        print("Warehouse refilled.")
        self.show_current_stock()

    def sell_product(self):
        self.show_current_stock()
        product_name = utils.ask_str("Enter the product name: ")
        product_quantity = -utils.ask_int("Enter the quantity: ", 100, 1)
        result = main_warehouse.change_product(product_name.strip(), product_quantity)

        match result:
            case ChangeProductStatus.SUCCESS:
                print(f"Successfully bought {abs(product_quantity)} of {product_name}.")
            case ChangeProductStatus.NOT_FOUND:
                print(f'Product "{product_name}" not found.')
            case ChangeProductStatus.NOT_ENOUGH:
                print(f'Not enough stock for "{product_name}".')

        utils.separator()
        self.show_current_stock()

        # print(f"Remaining stock: {main_warehouse.get_product_stock(product)}")
