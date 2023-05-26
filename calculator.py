from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, result)

# Create the Tkinter window
window = Tk()
window.title("Calculator")

# Create the entry field for display
entry = Entry(window, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
for i in range(10):
    button = Button(window, text=str(i), padx=20, pady=10, command=lambda i=i: button_click(i))
    button.grid(row=(i+3)//3, column=(i-1)%3, padx=5, pady=5)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = Button(window, text=operator, padx=20, pady=10, command=lambda operator=operator: button_click(operator))
    button.grid(row=i+3, column=3, padx=5, pady=5)

# Create the clear button
button_clear = Button(window, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=2, column=0, padx=5, pady=5)

# Create the equal button
button_equal = Button(window, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()
