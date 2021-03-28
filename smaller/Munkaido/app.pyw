import timeing
from appendname import *
from request import *
import json
import info


class Arrive:
    # érkezés rögzítése
    def arrival(self):
        table = []
        label = Label(app, text="Kezdési idő rögzítve!", fg="red", font='Helvetica 8 bold')
        label.grid(row=5, column=0)
        data = {"name": worker.get(), "arriveDate": timeing.Timerecord().arrival()}
        table.append(data)
        Arrive.table = json.dumps(table, ensure_ascii=False)
        return Arrive.table

    def arriveSave(self):
        Arrive().arrival()
        with open('data\workinghours.json', "a") as working:
            working.write(Arrive.table)
            working.close()


class Depart:
    # távozás rögzítése
    def leaving(self):
        table = []
        label = Label(app, text="Végzési idő rögzítve", fg="red", font='Helvetica 8 bold')
        label.grid(row=5, column=2)
        data = {"name": worker.get(), "leaveDate": timeing.Timerecord().arrival()}
        table.append(data)
        Depart.table = json.dumps(table, ensure_ascii=False)
        return Depart.table

    def leaveSave(self):
        Depart().leaving()
        with open('data\workinghours.json', "a") as working:
            working.write(Depart.table)
            working.close()


# ablak létrehozása
app = Tk()
app.wm_iconbitmap('logo.ico')
app.wm_title("Munkaidő nyilvántartó")
app.after(1, lambda: app.focus_force())


#elements
label1 = Label(app, text='Munkaidő nyilvántartás', font='Helvetica 12 bold')
label2 = Label(app, text='Dolgozó kiválasztása', font='Helvetica 12 bold')
arriveButton = Button(app, text="Érkezés", width=15, height=2, command=Arrive().arriveSave, font='Helvetica 10 bold',
                      padx=10, pady=10)
leaveButton = Button(app, text="Távozás", width=15, height=2, command=Depart().leaveSave, font='Helvetica 10 bold',
                     padx=10, pady=10)


#menu
mainmenu = Menu(app)
submenu1 = Menu(app, tearoff=False)
submenu1.add_command(label="Dolgozó rögzítése", command=AddName().addname)
submenu1.add_command(label="Dolgozó törlése")
mainmenu.add_cascade(label="Dolgozók karbantartása", menu=submenu1)
submenu2 = Menu(app, tearoff=False)
submenu2.add_command(label="Egyszerű lekérdezés", command=Request().requestworker)
submenu2.add_command(label="Összetett lekérdezés")
mainmenu.add_cascade(label="Lekérdezések", menu=submenu2)
mainmenu.add_command(label="Névjegy", command=info.information)
app.config(menu=mainmenu)


# A dolgozók nevei
worker = StringVar()
w = OptionMenu(app, worker, "Győri Gábor", "Kiss Péter", "Győri Imre")
worker.set('Dolgozó kiválasztása...')


# megjelenítés az ablakban
label1.grid(row=0, column=1)
w.grid(row=1, column=1)
arriveButton.grid(row=2, column=0, sticky=W, pady=10)
leaveButton.grid(row=2, column=2, sticky=W, pady=10)


mainloop()
