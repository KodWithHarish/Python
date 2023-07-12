# grid
from tkinter import *
from tkinter import ttk

root = Tk()

label1 = Label(root,text = 'label 1',bg = 'red')
label1.grid(row = 0,column = 0 ,sticky = W+E)

label2 = Label(root,text = 'label 2',bg = 'green')
label2.grid(row = 0,column = 1,ipadx = 50 , ipady = 50)

label3 = Label(root,text = 'label 3',bg = 'blue')
label3.grid(row = 1,column = 0,ipadx = 50 , ipady = 50)

label4 = Label(root,text = 'label 4',bg = 'pink')
label4.grid(row = 1,column = 1,ipadx = 20 , ipady = 20,sticky = SE)

root.mainloop()


