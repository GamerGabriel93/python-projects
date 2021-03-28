from tkinter import *
import webbrowser

with open("copyright.txt", "r", encoding="utf8") as file:
    copyright = file.read()
    file.close()


def callback(url):
    webbrowser.open_new(url)


def information():
    info = Tk()
    info.geometry("300x180")
    info.wm_title('Névjegy')
    info.after(1, lambda: info.focus_force())
    info.wm_iconbitmap('logo.ico')
    Label(info, text=copyright, font="Arial 10 bold", justify=CENTER).pack(pady=5)
    """label2 = Label(info, text="Github", font="Arial 10 bold", fg='red', wraplength=300, cursor="hand2", justify=CENTER)
    label2.bind("<Button-1>", lambda e: callback("https://github.com/GamerGabriel93/python-projects"))
    label2.pack()"""

    mainloop()
