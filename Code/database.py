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
tkWindow.title('O.S.M.A Database (TO BE MADE)')


Label(tkWindow, text=("O.S.M.A Database: ERROR 3"), relief=FLAT).grid(row=3, column=2)
tkWindow.mainloop()