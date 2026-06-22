# numbers = []
# operators = []

statement = input("Enter the statement: ")
value = eval(statement)
print("The value is:", value)
# # Separate numbers and operators
# for char in statement:
#     try:
#         numbers.append(int(char))
#     except ValueError:
#         operators.append(char)

# # Start with the first number
# value = numbers[0]

# # Perform calculations
# for i in range(len(operators)):
#     op = operators[i]

#     if op == '+':
#         value += numbers[i + 1]
#     elif op == '-':
#         value -= numbers[i + 1]
#     elif op == '*':
#         value *= numbers[i + 1]
#     elif op == '/':
#         value /= numbers[i + 1]

# print("The value is:", value)