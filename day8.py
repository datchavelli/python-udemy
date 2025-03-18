import sys

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]
print('''
                                  
   ___ __ _  ___  ___  __ _ _ __  
  / __/ _` |/ _ \/ __|/ _` | '__| 
 | (_| (_| |  __/\__ \ (_| | |    
  \___\__,_|\___||___/\__,_|_|    
      (_)     | |                 
   ___ _ _ __ | |__   ___ _ __    
  / __| | '_ \| '_ \ / _ \ '__|   
 | (__| | |_) | | | |  __/ |      
  \___|_| .__/|_| |_|\___|_|      
        | |                       
        |_|
    ''')
program_running = True
# encrypt() function 

def ceasar(original_text,shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else: 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Encoded result: {output_text}")

while program_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ").lower()
    if direction == "encode" or direction == "decode":
        shift = int(input("Type the shift number: \n"))
        sometext = input("Enter text to be coded: ").lower()
        ceasar(sometext,shift,direction)
    elif direction == "quit":
        print("Thanks for using the program")
        program_running = False
        sys.exit()
    else:
        print("Wrong input")
        program_running = False
        sys.exit()

