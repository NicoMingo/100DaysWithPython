from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

true_or_false = True

while(true_or_false):

    order_name = input("What would you like? (espresso/latte/cappuccino): ")
    
    if order_name == "report":
        coffee_maker.report()

    elif order_name == "report money":
        money_machine.report()
    
    elif order_name == "off":
        true_or_false = False
    
    else:
        order = menu.find_drink(order_name)
    
    # Aqui convertimos el string que nos retorna el metodo en una lista, y usamos el slicing operator porque cuando usamos el split el ultimo elemento de la lista es un " ", entonces con el slicing op eliminamos ese elemento
        if order_name in menu.get_items().split("/")[0:3]:
            
            if coffee_maker.is_resource_sufficient(order) == True:
                
                if money_machine.make_payment(order.cost) == True:
                    coffee_maker.make_coffee(order)
    