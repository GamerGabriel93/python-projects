from tkinter import *
import ido
import json


class Arrive:
    def erkezes(self):
        label = Label(root, text="Kezdési idő rögzítve!", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=0)
        with open('workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", ido.Idopontok().erkezes()), working, ensure_ascii=False)
            working.close()


class Depart:
    def tavozas(self):
        label = Label(root, text="Végzési idő rögzítve", fg="red", font='Helvetica 8 bold')
        label.grid(row=3, column=3)
        with open('workinghours.json', "a") as working:
            json.dump((f"{worker.get()}", ido.Idopontok().erkezes()), working, ensure_ascii=False)
            working.close()


root = Tk()
root.winfo_toplevel().title("Munkaidő nyilvántartó")
label1 = Label(root, text='Munkaidő nyilvántartás', font='Helvetica 12 bold')
erkButton = Button(root, text="Érkezés", width=15, height=3, command=Arrive().erkezes, font='Helvetica 10 bold', padx=20)
tavButton = Button(root, text="Távozás", width=15, height=3, command=Depart().tavozas, font='Helvetica 10 bold', padx=20)
worker = StringVar()
w = OptionMenu(root, worker, "Győri Gábor", "Győri Evelin", "Győri Imre", "Győri Imréné")
worker.set('Dolgozó kiválasztása')
label1.grid(row=0, column=1)
w.grid(row=1, column=1)
erkButton.grid(row=2, column=0, sticky=W)
tavButton.grid(row=2, column=3, sticky=W)

mainloop()
