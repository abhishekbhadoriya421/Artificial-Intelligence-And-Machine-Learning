
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

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")

result = calculations(num1, num2, operation)
print(f"The result is: {result}")