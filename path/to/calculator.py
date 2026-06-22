import math


# Basic Operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


# Powers and Roots
def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError("Cannot find square root of a negative number.")
    return math.sqrt(x)


# Logarithms
def logarithm(x):
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log10(x)


def natural_log(x):
    if x <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(x)


# Trigonometric Functions
def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


# Factorial
def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(int(x))


# Constants
def pi():
    return math.pi


def e():
    return math.e


# Dispatcher Function
def calculate(operation, *args):

    if operation == '+':
        return add(args[0], args[1])

    elif operation == '-':
        return subtract(args[0], args[1])

    elif operation == '*':
        return multiply(args[0], args[1])

    elif operation == '/':
        return divide(args[0], args[1])

    elif operation == '^':
        return power(args[0], args[1])

    elif operation == 'sqrt':
        return square_root(args[0])

    elif operation == 'log':
        return logarithm(args[0])

    elif operation == 'ln':
        return natural_log(args[0])

    elif operation == 'sin':
        return sine(args[0])

    elif operation == 'cos':
        return cosine(args[0])

    elif operation == 'tan':
        return tangent(args[0])

    elif operation == 'fact':
        return factorial(args[0])

    elif operation == 'pi':
        return pi()

    elif operation == 'e':
        return e()
    else:
        raise ValueError("Invalid operation")