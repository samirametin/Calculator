def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator(first, second, operation):
    if operation == "+":
        result = add(first, second)
    elif operation == "-":
        result = subtract(first, second)
    elif operation == "*":
        result = multiply(first, second)
    elif operation == "/":
        result = divide(first, second)
    return result


first_number = float(input("What's the first number?: "))
print("+", "-", "*", "/", sep="\n")
operation = input("Pick an operation: ")
second_number = float(input("What's the next number?: "))
answer = calculator(first_number, second_number, operation)
print(answer)
