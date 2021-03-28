from tkinter import *
import webbrowser

with open("copyright.txt", "r", encoding="utf8") as file:
    copyright = file.read()
    file.close()


def callback(url):
    webbrowser.open_new(url)


def information():
    info = Tk()
    info.geometry("300x300")
    info.wm_title('Lekérdezés')
    info.wm_iconbitmap('logo.ico')
    label1 = Label(info, text="Készítette: Győri Gábor 2021", font="Arial 12 bold",  wraplength=300, cursor="hand2")
    label2 = Label(info, text=copyright, font="Arial 12",  wraplength=300)
    label3 = Label(info, text="Elérhetőségek mutatása", font="Arial 12 bold", fg='red', wraplength=300)
    label3.bind("<Button-1>", lambda e: callback("https://google.hu"))
    label1.grid(row=0, column=0, pady=10)
    label2.grid(row=1, column=0, pady=10)
    label3.grid(row=2, column=0, pady=10)
    mainloop()


information()
