from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

chk_state1 = BooleanVar()
chk_state2 = BooleanVar()
chk_state3 = BooleanVar()
chk_state4 = BooleanVar()

chk_state2.set(True) #set check state

chk1 = Checkbutton(window, text='Car', var=chk_state1)
chk2 = Checkbutton(window, text='Mobile', var=chk_state2)
chk3 = Checkbutton(window, text='Home', var=chk_state3)
chk4 = Checkbutton(window, text='Bike', var=chk_state4)

chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)
chk4.grid(column=0, row=3)


#invert BOOLEAN states
chk_state1 = IntVar()
chk_state1.set(0) #uncheck
chk_state1.set(1) #check

window.mainloop()
