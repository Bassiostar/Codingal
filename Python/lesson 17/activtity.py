from tkinter import *
from tkinter import messagebox
from PTL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload = Image.open("app_img.jpg")