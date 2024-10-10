import tkinter as tk
from tkinter import messagebox

# Create the main window
obj = tk.Tk()
obj.geometry("600x300")
obj.title("Operations")
obj.config(bg='blue')

# Define IntVar for inputs and result
num1 = tk.IntVar()
num2 = tk.IntVar()
num3 = tk.IntVar()  # This will store the result

# Define the add function
def add():
    a = num1.get()
    b = num2.get()
    result = a + b
    num3.set(result)
    messagebox.showinfo('Result', f'The sum is {result}')

# Define the subtract function
def subtract():
    a = num1.get()
    b = num2.get()
    result = a - b
    num3.set(result)
    messagebox.showinfo('Result', f'The difference is {result}')

# Define the multiply function
def multiply():
    a = num1.get()
    b = num2.get()
    result = a * b
    num3.set(result)
    messagebox.showinfo('Result', f'The product is {result}')

# Define the divide function
def divide():
    a = num1.get()
    b = num2.get()
    if b != 0:
        result = a / b
        num3.set(result)
        messagebox.showinfo('Result', f'The quotient is {result}')
    else:
        messagebox.showerror('Error', 'Cannot divide by zero')

# Add labels and entry widgets for user input
tk.Label(obj, text="Enter value A:", font=("calibri", 14), bg='blue', fg='white').grid(row=0, column=0, padx=10, pady=10)
tk.Entry(obj, textvariable=num1, font=("calibri", 14)).grid(row=0, column=1, padx=10, pady=10)

tk.Label(obj, text="Enter value B:", font=("calibri", 14), bg='blue', fg='white').grid(row=1, column=0, padx=10, pady=10)
tk.Entry(obj, textvariable=num2, font=("calibri", 14)).grid(row=1, column=1, padx=10, pady=10)

tk.Label(obj, text="Result:", font=("calibri", 14), bg='blue', fg='white').grid(row=2, column=0, padx=10, pady=10)
tk.Entry(obj, textvariable=num3, font=("calibri", 14)).grid(row=2, column=1, padx=10, pady=10)

# Add buttons for operations
tk.Button(obj, text="Add", command=add, font=("calibri", 14), bg='green', fg='white').grid(row=3, column=0, padx=10, pady=10)
tk.Button(obj, text="Subtract", command=subtract, font=("calibri", 14), bg='green', fg='white').grid(row=3, column=1, padx=10, pady=10)
tk.Button(obj, text="Multiply", command=multiply, font=("calibri", 14), bg='green', fg='white').grid(row=4, column=0, padx=10, pady=10)
tk.Button(obj, text="Divide", command=divide, font=("calibri", 14), bg='green', fg='white').grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter loop
obj.mainloop()
