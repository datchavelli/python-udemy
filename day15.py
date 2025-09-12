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

ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

choices = ["espresso","latte","cappuccino","report"]
money = 0

def pay():
    pennies = int(input("How many pennies? "))
    nickel = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    
    money = pennies*0.01 + nickel*0.05 + dimes*0.1 + quarters*0.25

    print(f"Money: {money}")

def buy_coffee(choice):
    if choice == "espresso":
        print(f"Espresso: ${MENU['espresso']['cost']}")
        print(f"Your money: {money}")
        if money < MENU['espresso']['cost']:
            print("Please enter more money")
            pay()
    elif choice == "late":
        print("Late")
    elif cappuccino == "cappuccino":
        print("Cappuccino")

def report():
    print(f"Water: {ressources['water']}")
    print(f"Milk: {ressources['milk']}")
    print(f"Coffee: {ressources['coffee']}")
    print(f"Money: ${money}")

def choose():
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "report":
        report()
    elif choice in choices:
        buy_coffee(choice)

choose()
