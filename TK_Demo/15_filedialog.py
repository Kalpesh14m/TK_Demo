from tkinter import *

from tkinter import filedialog

window = Tk()

window.title("Welcome to Kalpesh First app")

#Know File Path
file = filedialog.askopenfilename()

#Applay Filers
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

#Know Directory Path
dir = filedialog.askdirectory()

from os import path

file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

print(file)
