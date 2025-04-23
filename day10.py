import os

clear = lambda: os.system('cls')

calc_ascii = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
operations = [
    "+",
    "-",
    "*",
    "/"
]
end_program = False

def addition(a,b):
    return int(a) + int(b)

def subtraction(a,b):
    return int(a) - int(b)

def multiplication(a,b):
    return int(a) * int(b)

def division(a,b):
    return int(a) / int(b)

def do_calculation(a,b,operation):
    if operation == "+":
        return addition(a,b)
    elif operation == "-":
        return subtraction(a,b)
    elif operation == "*":
        return multiplication(a,b)
    elif operation == "/":
        return division(a,b)
    else:
        return False

print("Welcome to our calculator!")
print(calc_ascii)

while end_program == False:
    first_number = input("What is the first_number? ")
    print(*operations, sep = '\n')
    operation = input("Pick an operation: ")
    while operation not in operations:
        operation = input("Pick a valid operation: ")
    second_number = input("What is the next number? ")
    result = do_calculation(first_number,second_number,operation)
    if result is not False:
        print(f"{first_number} {operation} {second_number} = {result}")
        continuation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        while continuation == "y":
            print(*operations, sep = '\n')
            operation = input("Pick an operaiton: ")
            while operation not in operations:
                operation = input("Pick a valid operation: ")
            next_number = input("What's the next number?: ")
            result_next = do_calculation(result,next_number,operation)
            if result_next is not False:
                print(f"{result} {operation} {next_number} = {result_next}")
                result = result_next
            else:
                print("Error, result returned False")
            continuation = input(f"Type 'y' to continue calculating with {result_next}, or type 'n' to start a new calculation: ")
        if continuation == "n":
            clear()
            print(calc_ascii)
    else:
        print("Result returned False")
print(f"Result: {result}")

