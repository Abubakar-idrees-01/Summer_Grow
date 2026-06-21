def add(x, y):
    """Addition function."""
    return x + y

def subtract(x, y):
    """Subtraction function."""
    return x - y

def multiply(x, y):
    """Multiplication function."""
    return x * y

def divide(x, y):
    """Division function."""
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

if __name__ == '__main__':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        exit()

    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
        print("Result:", result)
    elif operation == '-':
        result = subtract(num1, num2)
        print("Result:", result)
    elif operation == '*':
        result = multiply(num1, num2)
        print("Result:", result)
    elif operation == '/':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid operator.")
