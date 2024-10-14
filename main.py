MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_resources(drink):
    if drink == "espresso":
        if MENU[drink]["ingredients"]["water"] <= resources["water"] and MENU[drink]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                return "There is not enough water"
            elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                return "There is not enough Coffee!"

    elif drink == "latte":
        if MENU[drink]["ingredients"]["water"] <= resources["water"] and MENU[drink]["ingredients"]["coffee"] <= resources["coffee"] and MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
            return True
        else:
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                return "There is not enough water"
            elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                return "There is not enough Coffee!"
            elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
                return "There is not enough Milk!"

    elif drink == "cappuccino":
        if MENU[drink]["ingredients"]["water"] <= resources["water"] and MENU[drink]["ingredients"]["coffee"] <= resources["coffee"] and MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
            return True
        else:
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                return "There is not enough water"
            elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                return "There is not enough Coffee!"
            elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
                return "There is not enough Milk!"
    else:
        return "No drink found !"

def turn_off():
    print("Turing the Machine OFF !")
    exit()

def report():
    print("Report:")
    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}")


def reduce_resources(drink):
    if drink == "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    elif drink == "latte":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    elif drink == "cappuccino":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def process_coins(quarters, dimes, nickles, pennies, drink):
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    cost_of_drink = MENU[drink]["cost"]
    if total >= cost_of_drink:
        global money
        money += cost_of_drink

        return f"Here's your change: {round(total - cost_of_drink, 2)}", 0 # 0 to know whether to know to deduct resources or not
    elif total < cost_of_drink:
        return "Sorry that's not enough money. Money refunded."


while True:
    user_wants = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_wants == "off":
        turn_off()
    elif user_wants == "report":
        report()
    elif user_wants == "espresso" or user_wants == "latte" or user_wants == "cappuccino":
        if check_resources(user_wants) == True:
            print("Please insert the coins!")
            quarters = int(input("Please insert quarters: "))
            dimes = int(input("Please insert dimes: "))
            nickles = int(input("Please insert nickles: "))
            pennies = int(input("Please insert pennies: "))
            print_message, return_value = process_coins(quarters, dimes, nickles, pennies, user_wants)
            if return_value == 0:
                reduce_resources(user_wants)
            print(print_message)

        else:
            print(check_resources(user_wants))