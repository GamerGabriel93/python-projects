from tkinter import *
import ido
import json


class Arrive:
    def erkezes(self):
        label = Label(root, text="Kezdési idő rögzítve!", fg="red")
        label.pack()
        with open('workinghours.json', "a") as working:
            json.dump(ido.Idopontok().erkezes(), working)
            working.close()


class Depart:
    def tavozas(self):
        label = Label(root, text="Végzési idő rögzítve", fg="blue")
        label.pack()
        with open('workinghours.json', "a") as working:
            json.dump(ido.Idopontok().erkezes(), working)
            working.close()


root = Tk()
root.geometry("400x300")
root.winfo_toplevel().title("Munkaidő nyilvántartó")
erkButton = Button(root, text="Érkezés", width=10, height=3, command=Arrive().erkezes)
tavButton = Button(root, text="Távozás", width=10, height=3, command=Depart().tavozas)
erkButton.place(relx=0, rely=0.8)
tavButton.place(relx=0.8, rely=0.8)

mainloop()
