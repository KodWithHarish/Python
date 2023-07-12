from tkinter import  *
def clearText():
    entry.delete(0,END)

def showText():
    labelText.set(entry.get())

root = Tk()

Label(root, text = 'What is your name').pack()
entry = Entry(root,bg = 'red',fg = 'white')
entry.pack()

Button(root,text = "Clear",command = clearText).pack()
Button(root,text = "change label",command = showText).pack()

labelText = StringVar()
labelText.set('label')

label = Label(root,textvariable = labelText)
label.pack()

root.mainloop()
