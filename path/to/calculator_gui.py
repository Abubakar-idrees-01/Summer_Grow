import tkinter as tk
from math_functions import evaluate


def press(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = evaluate(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history.insert(tk.END, f"{result}\n")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ---------------- UI ----------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x600")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

history = tk.Text(root, height=5)
history.pack(fill="both", padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/", "sin("],
    ["4", "5", "6", "*", "cos("],
    ["1", "2", "3", "-", "tan("],
    ["0", ".", "(", ")", "+"],
    ["sqrt(", "log(", "ln(", "^", "pi"],
    ["e", "fact(", "C", "="]
]

frame = tk.Frame(root)
frame.pack()

for r, row in enumerate(buttons):
    for c, btn in enumerate(row):

        if btn == "=":
            action = calculate
        elif btn == "C":
            action = clear
        else:
            action = lambda x=btn: press(x)

        tk.Button(
            frame,
            text=btn,
            width=7,
            height=2,
            command=action
        ).grid(row=r, column=c, padx=3, pady=3)

root.mainloop()