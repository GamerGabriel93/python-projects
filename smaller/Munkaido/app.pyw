import timeing
from appendname import *
from request import *
import json
import time


class Arrive:
    # érkezés rögzítése
    def arrival(self):
        label = Label(app, text="Kezdési idő rögzítve!", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=0)
        with open('data\workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", timeing.Timerecord().arrival()), working, ensure_ascii=False)
            working.close()


class Depart:
    # távozás rögzítése
    def leaving(self):
        label = Label(app, text="Végzési idő rögzítve", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=2)
        with open('data\workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", timeing.Timerecord().leaving()), working, ensure_ascii=False)
            working.close()


def workers():
    f = open('data\workers.json', 'r', encoding='UTF8')
    nevek = json.loads(f.read())
    f.close()
    workers.nevek = nevek['names']
    lst = []
    for i in range(0, len(workers.nevek)):
        lst.append(workers.nevek[i]['name'])
        i += 1
    return lst


# ablak létrehozása
app = Tk()
app.wm_iconbitmap('logo.ico')
app.wm_title("Munkaidő nyilvántartó")
label1 = Label(app, text='Munkaidő nyilvántartás', font='Helvetica 12 bold')
arriveButton = Button(app, text="Érkezés", width=15, height=2, command=Arrive().arrival, font='Helvetica 10 bold',
                      padx=10)
leaveButton = Button(app, text="Távozás", width=15, height=2, command=Depart().leaving, font='Helvetica 10 bold',
                     padx=10)
new_worker = Button(app, text="Dolgozó hozzáadása", width=15, height=1, command=AddName().addname,
                    font='Helvetica 10', padx=10)
request = Button(app, text="Dolgozó lekérdezése", width=15, height=1, command=Request().requestworker,
                 font='Helvetica 10', padx=10)

# A dolgozók nevei
worker = StringVar()
w = OptionMenu(app, worker, "Győri Gábor", "Kiss Péter", "Győri Imre", "dolgozók", workers())
worker.set('Dolgozó kiválasztása')

# megjelenítés az ablakban
label1.grid(row=0, column=1)
new_worker.grid(row=1, column=0)
w.grid(row=1, column=1)
request.grid(row=1, column=2)
arriveButton.grid(row=2, column=0, sticky=W)
leaveButton.grid(row=2, column=2, sticky=W)

mainloop()
