import math
from functools import reduce

def add(user_input):
    return reduce((lambda x,y: int(x)+int(y)), user_input)

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return (num1**2)

def cube(num1):
    return (num1**3)

def power(num1, num2):
    return math.pow(num1, num2)

def mod(num1, num2):
    return num1 % num2
