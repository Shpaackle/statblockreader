import tkinter as tk
from tkinter import ttk


win = tk.Tk()  # Create instance
win.title("Stat Block Reader")  # Add a title

# win.resizable(0, 0)  # Disable resizing the GUI

# Adding a Label
# ttk stands for "themed tk". It improves GUI look and feel.
# a_label = ttk.Label(win, text="A Label")
# a_label.grid(column=0, row=0)


# Button Click Event Callback Function
def click_me():
    message = "Hello " + name.get() + " " + numberChosen.get()
    action.configure(text=message)


# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
# Position Button in second row, second column (zero-based)
action.grid(column=2, row=1)

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()  # Place cursor into name Entry

# action.configure(state="disabled")  # Disable the Button Widget

"""
We are inserting another column between the Entry widget and the Button using the grid layout manager
"""
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
# state="readonly" stops user added values in Combobox
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

win.mainloop()  # Start GUI
