from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)

#Give placeholder text
txt.insert(INSERT,'You text goes here')

txt.delete(1.0,END)

txt.grid(column=0,row=0)

window.mainloop()
