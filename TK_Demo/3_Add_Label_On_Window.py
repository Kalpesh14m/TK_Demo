from tkinter import *

#Call TK mehton to initiate window
window = Tk()

window.title("Welcome to Kalpesh First app")

#Set window size
window.geometry('350x200')


#Set Label on window
lbl = Label(window, text="Hello")

#Set label on window at position (0,0)
lbl.grid(column=0, row=0)

window.mainloop()
