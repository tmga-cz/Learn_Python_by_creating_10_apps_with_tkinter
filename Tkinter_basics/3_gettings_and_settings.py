import tkinter as tk
from tkinter import ttk

def button_func():
    #get content of the entery
    entry_text = entry.get()

    #update the label
    # label.configure(text = 'some other text') #1.moznost
    # label['text'] = 'some other text' #2 moznost
    label['text'] = entry_text

    entry['state'] = 'disabled'    

    print(label.configure()) #zobrazí všechny atributy pro label


#window
window = tk.Tk()
window.title('Getting and setting widgets')

#widgets
label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The button', command=button_func)
button.pack()

#run
window.mainloop()
