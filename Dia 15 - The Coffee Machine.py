MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}



def check_resources(drink):
    global resources
    
    counter = 0
    for key in resources.keys():
        if drink["ingredients"][key] < resources[key]:
            counter += 1
        else:
            if counter == 0:
                print("Sorry there's not enough water.")
            elif counter == 1:
                print("Sorry there's not enough milk.")
            elif counter == 2:
                print("Sorry there's not enough coffee.")
            return False
        
        if counter == 3:
            return True


def machine_working(order):
    print("Please insert coins.")
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickles = int(input("How many nickles?: "))
    user_pennies = int(input("How many pennies?: "))
    total_amount = user_quarters * 0.25 + user_dimes * 0.1 + user_nickles * 0.05 + user_pennies * 0.01
    
    if total_amount > MENU[order]["cost"]:

        for key in resources.keys():
                if key != "money":
                    resources[key] -= MENU[order]["ingredients"][key]

        change = total_amount - MENU[order]["cost"]
        resources["money"] += total_amount - change
        print(f"Here is ${change:.2f} in change.")
        print("Here is your espresso ☕ Enjoy!!")
    else:
        print("Sorry that's not enough money. Money refunded.")


true_or_false = True

while(true_or_false):

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        for key, value in resources.items():
            if key == "coffee":
                print(f"{key}: {value}g")
            elif key == "money":
                print(f"{key}: ${value:.2f}")
            else:
                print(f"{key}: {value}ml")
    
    elif order in list(MENU.keys()):
        if check_resources(MENU[order]) == True:
            machine_working(order)

    elif order == "off":
        true_or_false = False