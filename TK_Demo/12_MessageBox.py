from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Welcome to Kalpesh First app")

window.geometry('350x200')

res1 = messagebox.askquestion('Message title','Message content4')
res2 = messagebox.askyesno('Message title','Message content5')
res3 = messagebox.askyesnocancel('Message title','Message content6')
res4 = messagebox.askokcancel('Message title','Message content7')
res5 = messagebox.askretrycancel('Message title','Message content8')

def clicked():
    messagebox.showinfo('Message title', 'Message content1')
    messagebox.showwarning('Message title', 'Message content2')  #shows warning message
    messagebox.showerror('Message title', 'Message content3')    #shows error message

btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)

window.mainloop()
