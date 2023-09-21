from site import execusercustomize
import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

#list of events
#pythontutorial.net/tkinter/tkinter-event-binding

#setup
window = tk.Tk()
window.geometry('600x500')
window.title('Combo and Spin')

#combobox
items = ('Ice cream', 'Pizza', 'Brocoli')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items #1 zpusob
#combo.configure(values=items) #2 způsob
combo.pack()

#evemts
#combo.bind('<<ComboboxSelected>>', lambda event: print(food_string.get()))
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

# combo_label = ttk.Label(window, text = 'a label', textvariable = food_string)
combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# Spinbox

#spin['value'] = (1,2,3,4,5)
spin_int = tk.IntVar(value = 12)

spin = ttk.Spinbox(
    window,
    from_ = 3,
    to = 20,
    increment = 3,
    command = lambda: print(spin_int.get()),
    textvariable = spin_int)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()
#####################################################################
exercise_letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin = ttk.Spinbox(window, textvariable = exercise_string, values=exercise_letters)
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))


#run
window.mainloop()
