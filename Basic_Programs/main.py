# n = input("enter a no : ")
#
# for value in range(1,11):
#     mul = value * int(n)
#     # line = str(n) + " x " + str(value) + " = " + str(mul)
#     print(mul)

from tkinter import *
from tkinter import messagebox

def bgblue():
    labelText.set('h ')
    label.config(bg='blue')

def bggreen():
    labelText.set('h ')
    label.config(bg='green')

def bgred():
    labelText.set('h ')
    label.config(bg='red')

def bgyellow():
    labelText.set('h ')
    label.config(bg='yellow')

def bggray():
    labelText.set('h ')
    label.config(bg='gray')

def bgblue():
    labelText.set('h ')
    label.config(bg='blue')

def bggreen():
    labelText.set('h ')
    label.config(bg='green')

def bgred():
    labelText.set('h ')
    label.config(bg='red')

def bgyellow():
    labelText.set('h ')
    label.config(bg='yellow')

def bggray():
    labelText.set('h ')
    label.config(bg='gray')

def clearText():
    entry.delete(0,END)

def showText():
    labelText.set(entry.get())

root = Tk()

Label(root, text = 'Enter a number').pack()
entry = Entry(root,bg = 'white',fg = 'black')
entry.pack()

Button(root,text = "Clear",command = clearText).pack()
Button(root,text = "Show Table",command = showText).pack()

labelText = StringVar()
labelText.set('h ')

labelText = StringVar()
labelText.set('h ')

labelText = StringVar()
labelText.set('h ')

labelText = StringVar()
labelText.set('h ')

label = Label(root,textvariable = labelText)
label.pack()

root.mainloop()

