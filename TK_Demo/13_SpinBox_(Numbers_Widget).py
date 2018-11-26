from tkinter import *

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

spin = Spinbox(window, from_=0, to=100, width=5)

spin1 = Spinbox(window, values=(3, 8, 11), width=5)

var =IntVar()
var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

spin.grid(column=0,row=0)
spin1.grid(column=2,row=0)
spin2.grid(column=4,row=0)

window.mainloop()
