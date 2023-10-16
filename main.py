def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


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
    for key in operations:
        print(key)
    operation_sign = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    calculator_function = operations[operation_sign]
    answer = calculator_function(first_number, second_number)
    print(f"{first_number} {operation_sign} {second_number} = {answer}")
    do_again = input(
        f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' for end calculation: "
    )
