from tkinter import *

#main program
app = Tk()
app.wm_title("Programom")
app.geometry("800x600")

#welcome text load from file
with open("welcome.txt", "r", encoding="utf8") as file:
    welcome = file.read()
    file.close()


def menucallback():
    print("I'm in the menu callback!")


def submenucallback():
    print("I'm in the submenu callback!")


#elements
main = Frame(app)
pageTitle = Label(main, text="Bejelentkezési felület", font='Arial 14 bold')
pageDescription = Label(main, text=welcome, font='Arial 12 bold')
username = Entry(main)
pw = Entry(main)
loginbutton = Button(main, text='Bejelentkezés')
registration = Button(main, text='Regisztráció')
forgetpw = Button(main, text='Elfelejtett jelszó')

#menu
mainmenu = Menu(app)
submenu = Menu(app, tearoff=False)
submenu.add_command(label="Submenu1", command=submenucallback)
submenu.add_command(label="Submenu2", command=submenucallback)
mainmenu.add_cascade(label='Item1', menu=submenu)
mainmenu.add_command(label="Item2", command=menucallback)
mainmenu.add_command(label="Item3", command=menucallback)
app.config(menu=mainmenu)

#show-elements
main.grid(row=0, column=0)
pageTitle.grid(row=0, column=0)
pageDescription.grid(row=1, column=0)
username.grid(row=2, column=0, padx=20, pady=5)
pw.grid(row=3, column=0, pady=5)
loginbutton.grid(row=4, column=0, pady=5)
registration.grid(row=5, column=0,pady=5)
forgetpw.grid(row=6, column=0)

#running
app.mainloop()


"""import Tkinter
parent_widget = Tkinter.Tk()
def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")
menu_widget = Tkinter.Menu(parent_widget)
submenu_widget = Tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Submenu Item1",
                           command=submenu_callback)
submenu_widget.add_command(label="Submenu Item2",
                           command=submenu_callback)
menu_widget.add_cascade(label="Item1", menu=submenu_widget)
menu_widget.add_command(label="Item2",
                        command=menu_callback)
menu_widget.add_command(label="Item3",
                        command=menu_callback)
parent_widget.config(menu=menu_widget)
Tkinter.mainloop()"""