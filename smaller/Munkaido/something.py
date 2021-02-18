from tkinter import *
import ido


class Arrive:
    def erkezes(self):
        ido.Idopontok().erkezes()
        label = Label(root, text="Kezdési idő rögzítve!", fg="red")
        label.pack()


class Depart:
    def tavozas(self):
        ido.Idopontok().erkezes()
        label = Label(root, text="Végzési idő rögzítve", fg="blue")
        label.pack()


root = Tk()
root.geometry("400x300")
root.winfo_toplevel().title("Munkaidő nyilvántartó")
erkButton = Button(root, text="Érkezés", width=10, height=3, command=Arrive().erkezes)
tavButton = Button(root, text="Távozás", width=10, height=3, command=Depart().tavozas)
erkButton.place(relx=0, rely=0.8)
tavButton.place(relx=0.8, rely=0.8)

mainloop()
