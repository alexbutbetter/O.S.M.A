# O.S.M.A is pretty barebones and lacks alot of functions so this extension adds alot of functions. It's a work in progress thing so I hope to get 20-25% done by the end of my spring break. Help is always well... helpful. I hope this will make O.S.M.A more usable in a medical space. Good luck and ciao!

# btw so far this only has the about bar so only look at comment above for some info

from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk, Tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import subprocess
import sys
from tkinter import messagebox as mb 
from turtle import exitonclick

tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg'] = 'white'

tkWindow.columnconfigure(0, weight=1)
tkWindow.columnconfigure(1, weight=3)

tkWindow.resizable(False, False)
s = ttk.Style()
tkWindow.tk.call("source", "azure.tcl")
tkWindow.tk.call("set_theme", "dark")
tkWindow.iconphoto(False, tkinter.PhotoImage(file='Untitled.png'))
tkWindow.title('O.S.M.A Database (W.I.P)')

# Menubar and Definitions 

def about():
    mb.showinfo('O.S.M.A Database', 'Extension to O.S.M.A which is basically a program that allows you to add more functions into O.S.M.A like a list of illnesses, meds, etc.')




def dbFunc():
    mb.error('ERROR 1', 'ERROR 1 CHECK WIKI AND OR HELP PAGE')

menubar = Menu(tkWindow)
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command = about())
aboutmenu.add_cascade(label="About", menu=aboutmenu)

# funny things to click on
BTN = Button(tkWindow,
             text='Dodaj nowego pacjenta ',
             #height=5,
             #width=10,
             command=dbFunc)

BTN.pack

tkWindow.config(menu=menubar)
tkWindow.mainloop()