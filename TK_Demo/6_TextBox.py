from tkinter import *

#Call TK mehton to initiate window
window = Tk()

window.title("Welcome to Kalpesh First app")
window.geometry('350x200')

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

#Disable textbox
txt1 = Entry(window,width=10, state='disabled')
txt1.grid(column=1, row=1)

window.mainloop()
