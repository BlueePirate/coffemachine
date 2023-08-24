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


def report():
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}ml")
    print(f"Money:${resources['money']}")
    return


def check_resources(user_choice):
    for item in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][item] >= resources[item]:
            print("Sorry there are not enough resources to make it. ")
            return False
        else:
            resources[item] -= MENU[user_choice]["ingredients"][item]
    return True


def calculate_money(user_choice):
    print("please insert the coins. ")
    no_of_quarters = int(input("How many quarters? "))
    no_of_dimes = int(input("How many dimes? "))
    no_of_nickles = int(input("How many nickles? "))
    no_of_pennies = int(input("How many pennies? "))
    total_money = 0.25*no_of_quarters + no_of_dimes*0.1 + no_of_nickles*0.05 + no_of_pennies*0.01
    if total_money >= MENU[user_choice]["cost"]:
        resources["money"] = resources["money"] + MENU[user_choice]["cost"]
        change = total_money-MENU[user_choice]["cost"]
        return round(change, 2)
    else:
        return 0


resources["money"] = 0
machine_on = True
while machine_on:
    user_choice = input("What would you like to have? 'espresso', 'latte', 'cappuccino'. ").lower()
    if user_choice == "report":
        report()
    elif user_choice == "off":
        machine_on = False
    else:
        enough_resources = check_resources(user_choice)
        if enough_resources:
            result_money = calculate_money(user_choice)
            if result_money >= 0:
                print(f"Here is ${result_money} change. ")
                print("Here is your coffee.☕")
            else:
                print("Sorry, that's not enough money.Money refunded. ")

