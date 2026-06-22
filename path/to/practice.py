def evaluate(expression):
    # Convert expression into tokens
    tokens = []
    number = ""

    for char in expression:
        if char.isdigit():
            number += char
        else:
            if number:
                tokens.append(int(number))
                number = ""

            if char != " ":
                tokens.append(char)

    if number:
        tokens.append(int(number))

    # Solve expressions inside brackets first
    while "(" in tokens:
        close_index = tokens.index(")")

        # Find matching opening bracket
        open_index = close_index
        while tokens[open_index] != "(":
            open_index -= 1

        # Evaluate expression inside brackets
        result = calculate(tokens[open_index + 1:close_index])

        # Replace bracketed expression with result
        tokens = (
            tokens[:open_index]
            + [result]
            + tokens[close_index + 1:]
        )

    return calculate(tokens)


def calculate(tokens):
    # Multiplication and division first
    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            result = tokens[i - 1] * tokens[i + 1]
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i = 0
        elif tokens[i] == "/":
            result = tokens[i - 1] / tokens[i + 1]
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i = 0
        else:
            i += 1

    # Addition and subtraction
    value = tokens[0]

    i = 1
    while i < len(tokens):
        if tokens[i] == "+":
            value += tokens[i + 1]
        elif tokens[i] == "-":
            value -= tokens[i + 1]

        i += 2

    return value


statement = input("Enter the expression: ")

answer = evaluate(statement)

print("The value is:", answer)