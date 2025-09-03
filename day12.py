import os
import sys
import random

print("Welcome to the Number Guessing Game! \n")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
difficulty_types = ['easy','hard']
if difficulty not in difficulty_types:
    print("Wrong Input. Run the program again and type the right input.")
    sys.exit()

random_number = random.randint(1,100)
attempts = 10

if difficulty == 'hard':
    attepmts = 5

print(f"You chose the {difficulty} difficulty")
print(f"You have {attempts} attempts.")

while attempts > 0:
    guess = int(input("Guess the number: "))
    if guess == random_number:
        print(f"CORRECT! You WON! It was the number {guess}")
        sys.exit()
        break
    else:
        attempts -= 1
        print(f"Wrong... You have {attempts} more left. Try again ")
        if guess > random_number:
            print("Try a lower number.")
        else:
            print("Try a higher number.")


print(f"Sorry you Lose. You haven't found the number {random_number}")
sys.exit()
