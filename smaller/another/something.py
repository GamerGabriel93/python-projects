from tkinter import *
import sqlite3
from datetime import datetime


class Workers:
    def currentTime(self):
        daytime = datetime.now()
        Workers.day = daytime.strftime("%Y.%m.%d")
        Workers.time = daytime.strftime("%H:%M")
        return Workers.day, Workers.time

    def save(self):
        Workers().currentTime()
        conn = sqlite3.connect("database.db")
        curs = conn.cursor()
        curs.execute('insert into naplo(nev,nap,erkezesiIdo) values (?,?,?)', (name.get(), Workers.day, Workers.time))
        conn.commit()
        conn.close()
        Label(app, text="Dolgozó rögzítve").grid(row=2, column=0)
        name['state'] = NORMAL
        name.delete(0, END)


app = Tk()
app.wm_title("Dolgozó rögzítése")
app.geometry("300x300")

name = Entry(app)
Button(app, text="Rögzítés", command=Workers().save).grid(row=1, column=0)
name.grid(row=0, column=0)

app.mainloop()
