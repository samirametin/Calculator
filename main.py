def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator_python():
    should_go_on = True
    first_number = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    while should_go_on:
        operation_sign = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculator_function = operations[operation_sign]
        answer = calculator_function(first_number, second_number)
        print(f"{first_number} {operation_sign} {second_number} = {answer}")
        do_again = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' for end calculation: "
        )
        if do_again == "y":
            first_number = answer
        elif do_again == "e":
            should_go_on = False
            print("Thanks for using our calculator! <3 <3 <3")
        elif do_again == "n":
            calculator_python()


calculator_python()
