from tkinter import *


class AddName:
    def addname(self):
        root = Tk()
        root.iconbitmap('logo.ico')
        root.geometry("300x100")
        root.winfo_toplevel().title("Dolgozó hozzáadása")

        ent = Entry(root)
        name = str(ent.get())
        button = Button(root, text="Rögzítés", command=AddName().record)
        button.place(relx=0.4, rely=0.5)

        ent.place(relx=0.3, rely=0.2)
        mainloop()

    def record(self):
        print(name)
        """with open('dolgozok.txt', 'a') as file:
            file.write(str(self.name))
            file.close()"""


nev = AddName()
nev.addname()
