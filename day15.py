import math
import sys
# Coffee Machine project

# Machie Setup

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
        "cost": 3,
    }
}

# You need to figure out how to use ressources
ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

choices = ["espresso","latte","cappuccino","report","quit"]
money = 0

def pay(choice):
    global money 
    if money < MENU[choice]['cost']:
        pennies = int(input("How many pennies? "))
        nickel = int(input("How many nickels? "))
        dimes = int(input("How many dimes? "))
        quarters = int(input("How many quarters? "))
        money += pennies*0.01 + nickel*0.05 + dimes*0.1 + quarters*0.25
    print(f"Money: ${money}")
    if money >= MENU[choice]['cost']:
        print("Enough")
        if money - MENU[choice]['cost'] == 0:
            print("Enjoy your drink, no change.")
            money = 0
            choose()
        else:
            print(f"Enjoy your drink, your change is: ${math.ceil(money-MENU[choice]['cost'])}")
            money = math.ceil(money-MENU[choice]['cost'])
            choose()
    else:
        print("Not enough the money")
        pay(choice)

def refil():
    print("Please refil!")
    water = int(input("How much water?: "))
    milk  = int(input("How much milk?: "))
    coffee= int(input("How much coffee?: "))

    if water + ressources['water'] > ressources['water']:
        ressources['water'] = 300
        print("Water overfilled")
    else:
        ressources['water'] += water
        print(f"Water added. Current water level: {ressources['water']}ml")
    if milk + ressources['milk'] > ressources['milk']:
        ressources['milk'] = 200
        print("Milk overfilled")
    else: 
        ressources['milk'] += milk
        print(f"Milk added. Current milk level: {ressources['milk']}ml")
    
    if coffee + ressources['coffee'] > ressources['coffee']:
        ressources['coffee'] = 100
        print("Coffee overfilled")
    else:
        ressources['coffee'] += coffee
        print(f"Coffee added. Current coffee level: {ressources['coffee']}mg")

def buy_coffee(choice):
    global ressources
    check_milk = False
    needs_refil = False

    if choice == "espresso":
        print("Espresso") 
    elif choice == "latte":
        print("Late")
        check_milk = True
    elif choice == "cappuccino":
        print("Cappuccino")
        check_milk = True
    else:
        print("Wrong input.")
        choose()

    if ressources['water'] - MENU[choice]['ingredients']['water'] > 0:
        print("Has water")
        ressources['water'] -= MENU[choice]['ingredients']['water']
    else:
        needs_refil = True
        print("Needs refil")
        refil()

    if ressources['coffee'] - MENU[choice]['ingredients']['coffee'] > 0:
        print("Has coffee")
        ressources['coffee'] -= MENU[choice]['ingredients']['coffee']
    else:
        needs_refil = True
        print("Needs refil")
        refil()

    if check_milk and ressources['milk'] - MENU[choice]['ingredients']['milk'] > 0:
        print("Has milk")
        ressources['milk'] -= MENU[choice]['ingredients']['milk']
    else:
        needs_refil = True
        print("Needs refil")
        refil()

    print(f"To pay: ${MENU[choice]['cost']}")
    print(f"Your money: {money}")
    if money < MENU['espresso']['cost']:
        print("Please enter more money")
    pay(choice)


def report():
    print(f"Water: {ressources['water']}")
    print(f"Milk: {ressources['milk']}")
    print(f"Coffee: {ressources['coffee']}")
    print(f"Money: ${money}")

def choose():
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "report":
        report()
    elif choice == "refil":
        refil()
    elif choice == "quit":
        sys.exit()
    elif choice in choices:
        buy_coffee(choice)
    else:
        print("Wrong input.")
        choose()

choose()
