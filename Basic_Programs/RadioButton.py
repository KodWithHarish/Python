# radio button
from tkinter import *

root = Tk()

def showvalue():
    print(value.get())

value = IntVar()  # StringVar()

Label(root ,text = 'where is taj mahal').pack()
Radiobutton(root,text = 'Delhi',value = 1 ,variable = value).pack()  # value = 'Delhi'
Radiobutton(root,text = 'Goa',value = 2,variable = value).pack()
Radiobutton(root,text = 'Mumbai',value = 3,variable = value).pack()
Radiobutton(root,text = 'Surat',value = 4,variable = value).pack()

Button(root,text = 'show id',command = showvalue).pack()
root.mainloop()
