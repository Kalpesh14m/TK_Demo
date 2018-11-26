from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

rad1 = Radiobutton(window,text='First', value=1)

rad2 = Radiobutton(window,text='Second', value=2)

rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

window.mainloop()
