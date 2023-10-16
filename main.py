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


is_go_on = True
do_again = "n"
while is_go_on:
    if do_again == "n":
        first_number = float(input("What's the first number?: "))
    elif do_again == "y":
        first_number = answer
    elif do_again == "e":
        print("Thanks for using our calculator! <3 <3 <3")
        break
    print("+", "-", "*", "/", sep="\n")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    answer = calculator(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {answer}")
    do_again = input(
        f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' for end calculation: "
    )
