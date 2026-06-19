from tkinter import *

# Create window
root = Tk()
root.title("NIWA'S CALCULATOR")zz
root.geometry("300x400")

# Display screen
screen = Entry(root, width=15, font=("Arial", 20),
               justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function for button clicks
def click(value):
    screen.insert(END, value)


# Function to calculate answer
def calculate():
    try:
        answer = eval(screen.get())
        screen.delete(0, END)
        screen.insert(END, answer)
    except:
        screen.delete(0, END)
        screen.insert(END, "Error")


# Function to clear screen
def clear():
    screen.delete(0, END)


# Button texts
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons automatically
row = 1
col = 0

for button in buttons:
    if button == '=':
        Button(root, text=button, width=5, height=2,
               command=calculate).grid(row=row,
                                       column=col,
                                       padx=5, pady=5)
    else:
        Button(root, text=button, width=5, height=2,
               command=lambda b=button: click(b)).grid(
                   row=row,
                   column=col,
                   padx=5, pady=5
               )

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
Button(root, text="C", width=25, height=2,
       command=clear).grid(row=5,
                           column=0,
                           columnspan=4,
                           padx=5, pady=5)

root.mainloop()