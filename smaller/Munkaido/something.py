from tkinter import *
import ido


root = Tk()
root.geometry("400x300")
root.winfo_toplevel().title("Munkaidő nyilvántartó")
erkButton = Button(root, text="Érkezés", width=10, height=3)
tavButton = Button(root, text="Távozás", width=10, height=3)
erkButton.place(relx=0, rely=0.8)
tavButton.place(relx=0.8, rely=0.8)

mainloop()
