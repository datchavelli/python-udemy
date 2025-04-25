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
end_program = False

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

print("Welcome to our calculator!")
print(calc_ascii)

def calculator():
    while end_program == False:
        first_number = float(input("What is the first_number?: "))
        print(*operations, sep = '\n')
        operation = input("Pick an operation: ")
        while operation not in operations:
            operation = input("Pick a valid operation: ")
        second_number = float(input("What is the next number?: "))
        result = operations[operation](first_number,second_number)
        if result is not False:
            print(f"{first_number} {operation} {second_number} = {result}")
            continuation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            while continuation == "y":
                print(*operations, sep = '\n')
                operation = input("Pick an operaiton: ")
                while operation not in operations:
                    operation = input("Pick a valid operation: ")
                next_number = float(input("What's the next number?: "))
                result_next = operations[operation](result,next_number)
                if result_next is not False:
                    print(f"{result} {operation} {next_number} = {result_next}")
                    result = float(result_next)
                else:
                    print("Error, result returned False")
                continuation = input(f"Type 'y' to continue calculating with {result_next}, or type 'n' to start a new calculation: ")
            if continuation == "n":
                clear()
                print(calc_ascii)
                calculator()
        else:
            print("Result returned False")
    print(f"Result: {result}")

calculator()
