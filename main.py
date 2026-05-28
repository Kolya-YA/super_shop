from shop import Shop
import utils

def main():
    shop_name = utils.ask_str("Enter the shop name or ENTER for default: ", 0)
    our_shop = Shop(shop_name)
    print(f"\nWelcome to {our_shop.name}!")
    print("—" * 20)

    while True:
        action = utils.ask_int("Enter an action:\n1 refill the warehouse\n2 sell products\n0 exit\n")
        match action:
            case 1:
                our_shop.refill_warehouse()
            case 2:
                our_shop.sell_product()
            case 0:
                exit()
            case _:
                print("Invalid action")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit,EOFError):
        print("\nBye!")
