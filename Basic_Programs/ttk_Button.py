# ttk button
from tkinter import *
from tkinter import ttk

root = Tk()

Button(root,text = 'button').pack()
ttk.Button(root,text = 'ttk button').pack()

root.mainloop()