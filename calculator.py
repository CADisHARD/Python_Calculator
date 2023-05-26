from tkinter import *

# Function to perform calculation
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = entry3.get()

    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    
    # Update the result label
    label_result.config(text="Result: " + str(result))

# Create the Tkinter window
window = Tk()
window.title("Calculator")

# Create entry fields for number input
entry1 = Entry(window, width=10)
entry1.pack(side=LEFT)

entry2 = Entry(window, width=10)
entry2.pack(side=LEFT)

entry3 = Entry(window, width=5)
entry3.pack(side=LEFT)

# Create button for calculation
button_calculate = Button(window, text="Calculate", command=calculate)
button_calculate.pack(side=LEFT)

# Create label for displaying result
label_result = Label(window, text="Result: ")
label_result.pack(side=LEFT)

# Run the Tkinter event loop
window.mainloop()
