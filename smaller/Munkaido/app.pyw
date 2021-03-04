import ido
from appendname import *
from request import *
import json


class Arrive:
    # érkezés rögzítése
    def erkezes(self):
        label = Label(app, text="Kezdési idő rögzítve!", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=0)
        with open('workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", ido.Idopontok().erkezes()), working, ensure_ascii=False)
            working.close()


class Depart:
    # távozás rögzítése
    def tavozas(self):
        label = Label(app, text="Végzési idő rögzítve", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=2)
        with open('workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", ido.Idopontok().erkezes()), working, ensure_ascii=False)
            working.close()


# ablak létrehozása
app = Tk()
app.wm_iconbitmap('logo.ico')
app.wm_title("Munkaidő nyilvántartó")
label1 = Label(app, text='Munkaidő nyilvántartás', font='Helvetica 12 bold')
erkButton = Button(app, text="Érkezés", width=15, height=2, command=Arrive().erkezes, font='Helvetica 10 bold',
                   padx=10)
tavButton = Button(app, text="Távozás", width=15, height=2, command=Depart().tavozas, font='Helvetica 10 bold',
                   padx=10)
ujdolgozo = Button(app, text="Dolgozó hozzáadása", width=15, height=1, command=AddName().addname,
                   font='Helvetica 10', padx=10)
lekerdezes = Button(app, text="Dolgozó lekérdezése", width=15, height=1, command=Request().requestworker,
                    font='Helvetica 10', padx=10)


# A dolgozók neveit ' vagy "-al kell kezdeni és zárni, a dolgozók nevei közé pedig ,-t tenni
worker = StringVar()
w = OptionMenu(app, worker, "Dolgozók nevei")
worker.set('Dolgozó kiválasztása')


# megjelenítés az ablakban
label1.grid(row=0, column=1)
ujdolgozo.grid(row=1, column=0)
w.grid(row=1, column=1)
lekerdezes.grid(row=1, column=2)
erkButton.grid(row=2, column=0, sticky=W)
tavButton.grid(row=2, column=2, sticky=W)


mainloop()
