
import math

class Calculator:

    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, operator, num2):

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print("Error: Please enter numbers.")
            raise ValueError("Invalid input")

        if operator not in self.operations:
            print("Error: Invalid operation.")
            raise ValueError("Invalid operation")

        try:
            return self.operations[operator](num1, num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            raise


# Advanced mathematical operations

def exponentiation(a, b):
    return a ** b

def square_root(a, b):
    return math.sqrt(a)

def logarithm(a, b):
    return math.log(a, b)


# Main program

calculator = Calculator()

calculator.add_operation("**", exponentiation)
calculator.add_operation("sqrt", square_root)
calculator.add_operation("log", logarithm)

while True:

    print("\nAvailable operations: +, -, *, /, **, sqrt, log")
    print("Type exit to stop.")

    operator = input("Enter operation: ")

    if operator.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        num1 = float(input("Enter first number: "))

        if operator not in ["sqrt"]:
            num2 = float(input("Enter second number: "))
        else:
            num2 = 0

        result = calculator.calculate(num1, operator, num2)

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers and try again.")
