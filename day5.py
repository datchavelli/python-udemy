import string
import random

letters_uppercase = list(string.ascii_uppercase)
letters_lowercase = list(string.ascii_lowercase)
letters = letters_lowercase + letters_uppercase
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]

user_choice1 = int(input("How many letters would you like in your password? "))
user_choice2 = int(input("How many symbols would you like? "))
user_choice3 = int(input("How many numbers would you like? "))

password_list = []

for char in range(0, user_choice1):
    password_list += random.choice(letters)

for number in range(0, user_choice2):
    password_list += random.choice(numbers)

for smybol in range(0,user_choice3):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

