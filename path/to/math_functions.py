import math

# Allowed scientific functions
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))

def sqrt(x):
    if x < 0:
        raise ValueError("No sqrt for negative number")
    return math.sqrt(x)

def log(x):
    if x <= 0:
        raise ValueError("log only for positive numbers")
    return math.log10(x)

def ln(x):
    if x <= 0:
        raise ValueError("ln only for positive numbers")
    return math.log(x)

def fact(x):
    if x < 0:
        raise ValueError("factorial only for positive numbers")
    return math.factorial(int(x))


# Safe evaluation environment
SAFE_ENV = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "sqrt": sqrt,
    "log": log,
    "ln": ln,
    "fact": fact,
    "pi": math.pi,
    "e": math.e,
    "__builtins__": {}
}


def evaluate(expression: str):
    """
    Evaluates full scientific expressions safely
    Example: 2+sin(30)*sqrt(16)
    """
    expression = expression.replace("^", "**")
    return eval(expression, SAFE_ENV)