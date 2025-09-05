import os
import sys
import random

print("Welcome to the Number Guessing Game! \n")
print("I'm thinking of a number between 1 and 100")

EASY_LVL = 10
HARD_LVL = 5

# Funciton to check users guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
    elif guess < actual_answer:
        print("Too Low")
    else:
        print(f"CORRECT! The answer was {actual_answer}")

# function to set difficulty 
def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    difficulty_types = ['easy','hard']
    if difficulty not in difficulty_types:
        print("Wrong Input. Run the program again and type the right input.")
        sys.exit()

    if difficulty == 'hard':
        return HARD_LVL
    else:
        return EASY_LVL


def game():

    random_number = random.randint(1,100)
    attempts = set_difficulty()
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

game()

