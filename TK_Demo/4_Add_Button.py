from tkinter import *

#Call TK mehton to initiate window
window = Tk()

window.title("Welcome to Kalpesh First app")

#Set window size
window.geometry('350x200')

btn = Button(window, text="Click Me")

#Change button Foreground color
btn = Button(window, text="Click Me", bg="Black", fg="Yellow")

btn.grid(column=1, row=0)

window.mainloop()
