from tkinter import *


class AddName:
    def addname(self):
        root = Tk()
        root.iconbitmap('logo.ico')
        root.geometry("300x100")
        root.winfo_toplevel().title("Dolgozó hozzáadása")

        namevar = StringVar()
        nev = namevar.get()
        nameentry = Entry(root, textvariable=nev)
        button = Button(root, text="Rögzítés")

        nameentry.place(relx=0.3, rely=0.2)
        button.place(relx=0.4, rely=0.5)
        mainloop()

    def recordname(self):
        with open('dolgozok.txt', 'a') as save:
            save.write(nev)
            save.close()
