from tkinter import *

from tkinter import Menu

window = Tk()

window.title("Welcome to Kalpesh First app")

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')

# new_item = Menu(menu, tearoff=0)

# new_item.add_command(label='New', command=clicked)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()
