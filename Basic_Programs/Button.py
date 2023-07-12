from tkinter import *
from tkinter import messagebox

def bgred():
    labelText.set('Red')
    label.config(bg = 'red')

def bggreen():
    labelText.set('Green')
    label.config(bg = 'green')

def bgblue():
    labelText.set('Blue')
    label.config(bg='blue')

root = Tk()
labelText = StringVar()
labelText.set('CHOOSE A COLOR')

label = Label(root, textvariable = labelText)
label.pack()

Button(root,text = "RED",command = bgred).pack()


Button(root,text = "GREEN",command = bggreen).pack()


Button(root,text = "BLUE",command = bgblue).pack()
root.mainloop()

