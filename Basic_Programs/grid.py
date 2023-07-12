# grid
from tkinter import *
from tkinter import ttk

root = Tk()

label1 = Label(root,text = 'label 1',bg = 'red')
label1.grid(row = 0,column = 0)

label2 = Label(root,text = 'label 2',bg = 'green')
label2.grid(row = 0,column = 1)

label3 = Label(root,text = 'label 3',bg = 'blue')
label3.grid(row = 0,column = 2)

label4 = Label(root,text = 'label 4',bg = 'pink')
label4.grid(row =0,column = 3)

label5 = Label(root,text = 'label 5',bg = 'red')
label5.grid(row =1,column = 0)

label6 = Label(root,text = 'label 6',bg = 'green')
label6.grid(row = 1,column = 1)

label7 = Label(root,text = 'label 7',bg = 'blue')
label7.grid(row = 1,column = 2)

label8 = Label(root,text = 'label 8',bg = 'pink')
label8.grid(row = 1,column = 3)

label9 = Label(root,text = 'label 9',bg = 'red')
label9.grid(row =2,column = 0)

label10 = Label(root,text = 'label 10',bg = 'green')
label10.grid(row = 2,column = 1)

label11= Label(root,text = 'label 11',bg = 'blue')
label11.grid(row = 2,column = 2)

label12= Label(root,text = 'label 12',bg = 'pink')
label2.grid(row = 2,column = 3)

root.mainloop()


