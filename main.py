from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def turn_off():
    print("Turing the Machine OFF !")
    exit()

money = MoneyMachine()
resources = CoffeeMaker()


latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

all_menu = Menu()
while True:
    user_wants = input(f"What would you like to order {all_menu.get_items()}?\n")
    if user_wants == "off":
        turn_off()
    elif user_wants == "report":
        resources.report()
        money.report()
    elif user_wants == "espresso" or user_wants == "latte" or user_wants == "cappuccino":
        obj_dict = {"espresso": espresso, "latte": latte, "cappuccino": cappuccino}
        if resources.is_resource_sufficient(obj_dict[user_wants]) == True:
            print(f"The cost of drink: {obj_dict[user_wants].cost}")
            if  money.make_payment(obj_dict[user_wants].cost) == True:
                resources.make_coffee(obj_dict[user_wants])

