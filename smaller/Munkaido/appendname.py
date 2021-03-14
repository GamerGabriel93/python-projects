from tkinter import *
import json


class AddName:
    name = ""

    def addname(self):
        AddName.root = Tk()
        AddName.root.iconbitmap('logo.ico')
        AddName.root.geometry("300x100")

        AddName.root.winfo_toplevel().title("Dolgozó hozzáadása")
        AddName.ent = Entry(AddName.root)
        AddName.button = Button(AddName.root, text="Rögzítés", command=AddName().record)

        AddName.button.place(relx=0.4, rely=0.5)
        AddName.ent.place(relx=0.3, rely=0.2)
        AddName.root.mainloop()

    def record(self):
        name = AddName.ent.get()
        with open('data\workers.json', 'a',  encoding='utf8') as file:
            json.dumps(file)
            file.close()
