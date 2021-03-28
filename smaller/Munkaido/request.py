from tkinter import *


class Request:
    def requestworker(self):
        Request.request = Tk()
        Request.request.geometry("300x300")
        Request.request.wm_title('Lekérdezés')
        Request.request.wm_iconbitmap('logo.ico')
        Request.request.after(1, lambda: Request.request.focus_force())

        Request.label = Label(Request.request, text="Dolgozó kiválasztása")
        Request.ent = Entry(Request.request)
        Request.button = Button(Request.request, text="Lekérdezés")

        Request.label.grid(row=0, column=0, padx=10, pady=10)
        Request.ent.grid(row=1, column=0, padx=10, pady=10)
        Request.button.grid(row=2, column=0, padx=10, pady=10)

        mainloop()
