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
        user_input = input_string.split(" ")
        operator = user_input.pop(0)
        print user_input

        """for num in user_input:
            num = int(num)"""

        if operator == "q":
            return
        elif operator == "+":
            result = add(user_input)
        elif operator == "-":
            result = subtract(user_input)
        elif operator == "*":
            result = multiply(user_input)
        elif operator == "/":
            result = divide(user_input)
        elif operator == "square":
            num1 = int(user_input[0])
            result = square(num1)
        elif operator == "cube":
            num1 = int(user_input[0])
            result = cube(num1)
        elif operator == "pow":
            num1 = int(user_input[0])
            num2 = int(user_input[1])
            result = power(num1, num2)
        elif operator == "mod":
            num1 = int(user_input[0])
            num2 = int(user_input[1])
            result = mod(num1, num2)
        print result

input_calculator()
    



