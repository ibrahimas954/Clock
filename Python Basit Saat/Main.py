from tkinter import *
from PIL import ImageTk,Image
import locale
import time

locale.setlocale(locale.LC_ALL, 'turkish')

root = Tk()
root.title('Saat')
root.geometry("800x600")

my_img = ImageTk.PhotoImage(Image.open("bayrak.png"))
my_laber = Label(image = my_img)
my_laber.pack(pady = 0)


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000,clock)

    my_label2.config(text = time_zone + "--" + day)

def update():
    my_label.config(text = "New Text")

my_label = Label(root, text = "", font =("Helvetica",52),fg = "green", bg = "black")
my_label.pack(pady = 20)

my_label2 = Label(root, text = "",font = ("Helvetica",14))
my_label2.pack(pady = 10)

my_label.after(5000, update())

clock()
root.mainloop()