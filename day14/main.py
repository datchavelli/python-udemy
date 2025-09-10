import game_data
import art
import random
import sys
import os

GAME_OVER = 0
compare_random = random.choice(game_data.data)
# Funkcija za poredjenje
def compare(choiceA,choiceB):
    # Izbor
    choice = input("Who has the bigger follower count? (A or B): ").upper()
    result = 0
    # Ako je A > B
    if choiceA['follower_count'] > choiceB['follower_count']:
        result = 1
    # Ako su A == B
    elif choiceA['follower_count'] == choiceB['follower_count']:
        compare_random = choiceB
        return True
    # Ako je B > A
    else:
        result = 2

    try: 
        if choice == "A" and result == 1:
            compare_random = choiceA
            return True
        elif choice == "B" and result == 2:
            compare_random = choiceB
            return True
        else:
            return False
    except ValueError:
        print("Wrong input! Answer with 'A' or 'B'")
        sys.exit()


def game():
    choice = True
    versus_compare = random.choice(game_data.data)
    while choice:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Stampa logoa igrice
        print(art.logo)
        #Stampa prvog odabranog
        print(f"Compare A: {compare_random['name']}, a {compare_random['description']} from {compare_random['country']}, follower count: {compare_random['follower_count']}mil")
        # Stampa VS-a 
        print(art.versus)
        # Stampa poredjenog
        print(f"With B: {versus_compare['name']}, a {versus_compare['description']} from {versus_compare['country']}")
        choice = compare(compare_random,versus_compare)
        if choice:
            versus_compare = random.choice(game_data.data)
            
    if compare_random['follower_count'] > versus_compare['follower_count']:
        print(f"Actually, you are wrong. {compare_random['name']} has {compare_random['follower_count']} mil and its more than {versus_compare['name']}'s {versus_compare['follower_count']} mil")
    else: 
        print(f"Actually, you are wrong. {versus_compare['name']} has {versus_compare['follower_count']} mil and its more than {compare_random['name']}'s {compare_random['follower_count']} mil")
game()
