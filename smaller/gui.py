from tkinter import *


def hello():
    x = 5
    y = 10


root = Tk()
text = Label(root, text="Kezdő program")
text.pack()
button = Button(root, text='Kattints', command=hello())
button.pack()

root.mainloop()
