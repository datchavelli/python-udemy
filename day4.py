import random
import sys

rps = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0,len(rps)-1)
user_choice = int(input("Rock (0), Paper (1), Scissors (2)! SHOOT: "))

asciiart = [
    """
    ROCK:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
    PAPER:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    """
    SCISSORS:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
]

print("You Put:")
print(asciiart[user_choice])
print("Computer Put:")
print(asciiart[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif user_choice == 1 and computer_choice == 0:
    print("YOU WIN")
elif user_choice == 2 and computer_choice == 1:
    print("YOU WIN!")
elif user_choice == computer_choice:
    print("ITS A DRAW!")
else:
    print("YOU LOSE")


