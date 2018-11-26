from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")#List of Items

combo.current(1) #set the selected item


#Get Selected item
def clicked():
   print(combo.get())

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=3, row=0)
combo.grid(column=0, row=0)

window.mainloop()
