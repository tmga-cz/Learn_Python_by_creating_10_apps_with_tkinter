import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)



#vytvoreni objektu window pro vytvoreni samotneho okna
#window = ttk.Window() 
#window = ttk.Window(themename = 'journal') #udela jine barvy v okně
window = ttk.Window(themename = 'darkly')
#window = tk.Tk()   #--->2.možnost

#nastaveni parametru okna
window.title('Demo')
window.geometry('600x200')

#title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold') #parametr master obvykle byva window
title_label.pack() #metoda prida label do okna, title_label zabalim do window

#input field
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar() #objekt pro držení proměné z Tknter Entery
entry = ttk.Entry(master = input_frame, textvariable= entry_int)#navazani na promenou nad kterou budu obsluhovat ve funkci convert
button = ttk.Button(master = input_frame, text = 'Convert', command=convert) #pozor funkci nevolat se zavorkama

entry.pack(side = 'left', padx = 10) #zabalim do input_framu, nastaveni padding x = 10 px
button.pack(side = 'left') #zabalim do input_framu
input_frame.pack(pady = 10) #input_frame zabalim do window

#output
output_string = tk.StringVar() #promena na vypsani
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable = output_string)

output_label.pack(pady=5)

#mainloop pro beh aplikace, aby hlavni okno hned nespadlo
window.mainloop()
