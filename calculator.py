"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def input_calculator():
    """Calculates user input

    Determines and solves mathematical expression based on user input"""
    while True:
        input_string = raw_input("> ") #what the user is entering
        tokens = input_string.split(" ")
        operator = tokens[0]

        if operator == "q":
            return
        elif operator == "+":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = add(num1, num2)
        elif operator == "-":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = subtract(num1, num2)
        elif operator == "*":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = multiply(num1, num2)
        elif operator == "/":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = divide(num1, num2)
        elif operator == "square":
            num1 = int(tokens[1])
            result = square(num1)
        elif operator == "cube":
            num1 = int(tokens[1])
            result = cube(num1)
        elif operator == "pow":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = power(num1, num2)
        elif operator == "mod":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            result = mod(num1, num2)
        print result

input_calculator()
    



