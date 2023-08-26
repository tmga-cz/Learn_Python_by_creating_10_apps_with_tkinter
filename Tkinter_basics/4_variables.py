import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window
window = tk.Tk()
window.title('Getting and setting widgets')


#tkinter variables
string_var = tk.StringVar(value='start value')
#int_var = tk.IntVar
#double_var = tk.DoubleVar
#boolean_var = tk.BooleanVar

#widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var) 
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

#run
window.mainloop()
