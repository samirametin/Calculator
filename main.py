first_number = float(input("What's the first number?: "))
print("+", "-", "*", "/", sep="\n")
operation = input("Pick an operation: ")
second_number = float(input("What's the next number?: "))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
