# check button
from tkinter import *
from tkinter import messagebox

root = Tk()

Label(root, text = 'what you would like to have it').pack()
Checkbutton(root, text = 'Milk').pack()
Checkbutton(root, text = 'Tea').pack()
Checkbutton(root, text = 'Coffee').pack()

root.mainloop()

