from tkinter import *

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
