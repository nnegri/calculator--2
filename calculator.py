"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input_string = raw_input("> ") #what the user is entering
    tokens = input_string.split(" ")
    operator = tokens[0]
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    input_calculator(operator, num1, num2)

def input_calculator(operator, num1, num2):
    """Calculates user input

    Determines and solves mathematical expression based on user input"""

    if operator == "q":
        break
    elif operator == "+":
        add(num1, num2)
    elif operator == "-":
        subtract(num1, num2)
    elif operator == "*":
        multiply(num1, num2)
    elif operator == "/":
        divide(num1, num2)
    elif operator == "square":
        square(num1)
    elif operator == "cube":
        cube(num1)
    elif operator == "pow":
        power(num1, num2)
    elif operator == "mod":
        mod(num1, num2)

