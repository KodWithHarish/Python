# label
from tkinter import *
from tkinter import messagebox
root = Tk()

def buttonTapped():
    messagebox._show('Message','Successfully Saved')

Button(root,text = 'Save',command = buttonTapped).pack()
root.mainloop()