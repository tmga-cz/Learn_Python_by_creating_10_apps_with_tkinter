import tkinter as tk
from tkinter import ttk


def button_func():
    print('a basic button')
    print(radio_var.get())

#window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button = ttk.Button(window, text = 'A simple button', command=lambda:print('a basic button 2. possibility'))
button_string=tk.StringVar(value='A button with string var')
button = ttk.Button(window, text = 'A simple button', command=button_func, textvariable=button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(
    window,
    text = 'checkbox 1', 
    command = lambda: print(check_var.get()),
    variable=check_var,
    onvalue = 10,
    offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command=lambda: check_var.set(5))
check2.pack()






#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 1',
    value=1,
    variable = radio_var,
    command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 2',
    value=2,
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio2.pack()

#radio another buttons
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

excercise_radio1 = ttk.Radiobutton(window, text='Radio A', value='A', command=radio_func, variable=radio_string)
excercise_radio2 = ttk.Radiobutton(window, text='Radio B', value='B', command=radio_func, variable=radio_string)
excercise_check = ttk.Checkbutton(window, text = 'excercise_check', variable=check_bool, command = lambda: print(radio_string.get()))

excercise_radio1.pack()
excercise_radio2.pack()
excercise_check.pack()


#run
window.mainloop()
