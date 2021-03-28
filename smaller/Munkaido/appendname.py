from tkinter import *
import json


class AddName:
    name = ""

    def addname(self):
        AddName.root = Tk()
        AddName.root.iconbitmap('logo.ico')
        AddName.root.geometry("300x100")
        AddName.root.after(1, lambda: AddName.root.focus_force())

        AddName.root.winfo_toplevel().title("Dolgozó hozzáadása")
        AddName.ent = Entry(AddName.root)
        Label(AddName.root, text="Név:").grid(row=0, column=0, padx=10, pady=10)
        AddName.button = Button(AddName.root, text="Rögzítés", command=AddName().record, width=10).grid(row=1, column=0, columnspan=2)
        AddName.label = Label(AddName.root, text="Dolgozó rögzítve", fg='red')

        AddName.ent.grid(row=0, column=1)
        AddName.root.mainloop()

    # A program futtatást követöen ez a metódust futtatja le rögzítéskor
    def record(self):
        name = AddName.ent.get()
        with open('data/workers.json', "r", encoding="UTF8") as file:
            originalworkernames = json.loads(file.readline())
            names = originalworkernames["workers"]
            newname= {"name": name}
            names.append(newname)
            workernames = {"workers": names}
            file.close()
        with open('data/workers.json', 'w',  encoding='utf8') as file:
            workernames = json.dumps(workernames, ensure_ascii=False)
            file.write(workernames)
            file.close()
        AddName.label.grid(row=2, column=0, columnspan=2)

        #a rögzítés után üresen hagyja a név mezőt
        """AddName.ent['state'] = NORMAL
        AddName.ent.delete(0, END)"""
