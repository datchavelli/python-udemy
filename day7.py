import random

from hangman_ascii import hangmanpics, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = "_" * word_length
lives = 7
tries = 0
game_over = False
all_letters_found = False
print(logo)
print("Dobrodosli u igru 'Vesalice'! Imate 7 zivota i morate da pogodite rec.")
print(f"Vasa rec je: {placeholder}")
print(f"{chosen_word}")
correct_letters = []

while not game_over:
    display = ""
    guess = input("Probajte da pogodite slovo: ")
    found_letter = False
    
    if len(guess) > 1 or guess == "" or guess == " ":
        lives -= 1
        print(f"Morate napisati jedno slovo. Izgubili ste zivot. Imate jos {lives}/7 zivota.")
        if lives <= 1 and found_letter == False:
            game_over = True
        print(hangmanpics[tries])
        tries += 1
        continue

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            found_letter = True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"{display}")
    i = 0
    
    if not "_" in display:
        game_over = True
        all_letters_found = True

    if lives == 1 and not found_letter:
        game_over = True
    if not found_letter:
        lives -= 1
        print(f"Nazalost to slovo nije u nasoj reci. Imate jos {lives}/7 zivota")
        print(hangmanpics[tries])
        tries += 1

if all_letters_found:
    print("Congratz!")
else:
    print("Izgubili ste")

