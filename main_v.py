import random

storefund = float(100)

class product:
    def __init__(self, name, selling_price, stock, buying_price):
        self.name = name
        self.selling_price = selling_price
        self.stock = stock
        self.buying_price = buying_price

    def __repr__(self):
        return self.name

class buyer:
    def __init__(self, budget, shopping_cart):
        self.budget = random.randint(1,40)
        self.shopping_cart = shopping_cart

all_products = [
    milk := product("milk", 3, 10, 1),
    bread := product("bread", 2, 10, 0.5),
    apple := product("apple", 0.3, 10, 0.1),
    water := product("water", 1, 10, 0.1),
    candy := product("candy", 2, 10, 1.5),
    cheese := product("cheese", 4, 10, 2)
]

def enter(lst):
    print(*lst, sep="\n")

x = random.choices(all_products, k = random.randint(1,12))

budget = random.randint(3,40)
cost_shoppingcart = 0
for p in x:
    cost_shoppingcart += p.selling_price

def frageallerfragen(can_afford):
    global storefund
    if can_afford == "yes":
        if budget >= cost_shoppingcart:
            print("The buyer can afford their shoppingcart!")
            storefund += cost_shoppingcart
        else:
            print("Wrong :( buyer can't afford their cart, storefund: -", cost_shoppingcart)
            storefund -= cost_shoppingcart
    elif can_afford == "no":
        if float(budget) < cost_shoppingcart:
            print("Correct, the buyer leaves the store in tears")
        else:
            print("You just lost your self a customer, pay attention next time!!")
    if can_afford != "yes" and can_afford != "no":
        print("Unclear response, please enter either yes or no")
        can_afford = input("Can the buyer afford their cart? (yes or no) ").lower()
        frageallerfragen(can_afford)

days = 0
customers_a_day = 0
def workday(days, customers_a_day):
    days += 1
    print("Day: ", days)
    while customers_a_day < 4:
        print("Current fund: ", storefund)
        print("New customer in store!!")
        print("Buyer budget:", budget)
        enter(x)
        print("Total cart cost: ", round(cost_shoppingcart, 2))
        can_afford = input("Can the buyer afford their cart? (yes or no) ").lower()
        frageallerfragen(can_afford)
        print("New fund: ", round(storefund, 2))
        print("")
        customers_a_day += 1

        print("Workday over! Time to check up on stock")
        #action = input("What would you like to do? (show stock, restock, next day")

#def feierabend_action(action):
    #if action == "show stock":
        #print("/n ---STOCK---") for p in all_products:
           # print(p.name, p.stock, "times in stock")
        #if action == "restock":


workday(days, customers_a_day)
