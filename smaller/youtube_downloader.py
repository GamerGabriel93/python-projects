from tkinter import *
import os
from pytube import YouTube


def download():
    link = inputbox.get()
    yt = YouTube(link)
    title = Label(main, text=yt.title)
    title.pack()
    leng_time = str(int(yt.length / 60)) + ":" + str(int(yt.length % 60))
    leng = Label(main, text=('Length of video is ' + str(leng_time) + ' minutes'))
    leng.pack()
    ys = yt.streams.get_highest_resolution()
    ys.download(cwd)
    download_complete = Label(main, text='Done!', fg='red', bg='white')
    download_complete.pack()
    saved = Label(main, text=('Saved to :' + str(cwd)), fg='red', bg='white')
    saved.pack()


cwd = os.getcwd()

main = Tk()
main.title('Youtube MP4 downloader')
main.geometry('400x200')

frame = Frame(main)
frame.pack()

download_button = Button(frame, text='Download', width=10, height=2, command=download, bg='red', fg='white')
download_button.pack()

info = Label(main, text='Please insert a link below than click to "Download" button', fg='red')
info.pack(side=TOP)


inputbox = Entry(main, bg='white', fg='red', width=100, justify='center')
inputbox.pack()


frame.mainloop()
