
def additions(num1,num2):
    return num1 + num2

def subtractions(num1,num2):
    return num1 - num2

def multiplications(num1,num2):
    return num1 * num2

def divisions(num1,num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def calculations(num1, num2, operation):
    match operation:
        case '+':
            return additions(num1, num2)
        case '-':
            return subtractions(num1, num2)
        case '*':
            return multiplications(num1, num2)
        case '/':
            return divisions(num1, num2)
        case _:
            return "Error: Invalid operation" 

exits = False
print("Welcome to the calculator!")
print("You can perform operations: +, -, *, / for exit type 'exit'")

num1 = float(input(""))
num2 = 0
while not exits:
    try:  
        operation = input("")
        num2 = float(input(""))
        if isinstance(num1, str) or isinstance(num2, str):
            print("Exiting the calculator. Goodbye!")
            exits = True
            break
        if operation.lower() == 'exit' or num1 == 'exit' or num2 == 'exit':
            exits = True
            break
        num1 = calculations(num1, num2, operation)
        print(f"{num1}")
    except ValueError or TypeError:
        print("Invalid input. Please enter numeric values for numbers.")