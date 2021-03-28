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

#elements
label1 = Label(app, text='Munkaidő nyilvántartás', font='Helvetica 12 bold')
label2 = Label(app, text='Dolgozó kiválasztása', font='Helvetica 12 bold')
arriveButton = Button(app, text="Érkezés", width=15, height=2, command=Arrive().arriveSave, font='Helvetica 10 bold',
                      padx=10, pady=10)
leaveButton = Button(app, text="Távozás", width=15, height=2, command=Depart().leaveSave, font='Helvetica 10 bold',
                     padx=10, pady=10)

#menu
mainmenu = Menu(app)
submenu = Menu(app, tearoff=False)
mainmenu.add_cascade(label="Dolgozó rögzítése", command=AddName().addname)
mainmenu.add_command(label="Lekérdezések", command=Request().requestworker)
mainmenu.add_command(label="Névjegy", command=info.information)
app.config(menu=mainmenu)


# A dolgozók nevei
worker = StringVar()
w = OptionMenu(app, worker, "Győri Gábor", "Kiss Péter", "Győri Imre")
worker.set('Dolgozó kiválasztása...')

"""scrollbar = Scrollbar(app)
listbox = Listbox(app, bg='white', yscrollcommand=scrollbar.set, width=50)
scrollbar.config(command=listbox.yview)
f = open('data\workers.json', 'r', encoding='UTF8')
nevek = json.loads(f.read())
f.close()
nevek = nevek['names']
for i in range(0, len(nevek)):
    listbox.insert(END, str(nevek[i]['firstname']))
listbox.grid(row=2, column=0, columnspan=3, pady=10)
scrollbar.grid(row=2, column=2)
value = str((listbox.get(ACTIVE)))"""


# megjelenítés az ablakban
label1.grid(row=0, column=1)
w.grid(row=1, column=1)
arriveButton.grid(row=2, column=0, sticky=W, pady=10)
leaveButton.grid(row=2, column=2, sticky=W, pady=10)


mainloop()
