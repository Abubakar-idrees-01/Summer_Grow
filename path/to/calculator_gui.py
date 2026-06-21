# calculator_gui.py
import tkinter as tk
from math_functions import add, subtract, multiply, divide

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        result_label.config(text=str(result))

    except ValueError:
        result_label.config(text="Invalid input")


root = tk.Tk()
root.title("Calculator GUI")

# Labels
label1 = tk.Label(root, text="Number 1:")
label1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()

# Entry fields
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
operation_var = tk.StringVar(value="+")
radio_plus = tk.Radiobutton(root, text="+", variable=operation_var, value="+")
radio_minus = tk.Radiobutton(root, text="-", variable=operation_var, value="-")
radio_multiply = tk.Radiobutton(root, text="*", variable=operation_var, value="*")
radio_divide = tk.Radiobutton(root, text="/", variable=operation_var, value="/")

radio_plus.pack()
radio_minus.pack()
radio_multiply.pack()
radio_divide.pack()


# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
