import tkinter as tk
from tkinter import ttk


def button_func(entry_string):
    print('a basic button was pressed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func
#setup
window = tk.Tk()
window.title('buttons, functions and arguments')


#widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()


#1 button = ttk.Button(window, text = 'A simple button', command=lambda:button_func(entry_string))
button = ttk.Button(window, text = 'A simple button', command=outer_func(entry_string))
button.pack()

#run
window.mainloop()
