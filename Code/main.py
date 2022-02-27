# O.S.M.A 

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

#Global varible to store the row poition of the label
CURRENT_LABEL_ROW =0


# Initial window setup
tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg'] = 'white'

tkWindow.resizable(False, False)
s = ttk.Style()
tkWindow.tk.call("source", "azure.tcl")
tkWindow.tk.call("set_theme", "dark")
tkWindow.iconphoto(False, tkinter.PhotoImage(file='Untitled.png'))
tkWindow.title('O.S.M.A')



# configure the grid columns and weights
tkWindow.columnconfigure(0, weight=1)
tkWindow.columnconfigure(1, weight=3)


# Function Definitions

active = print("O.S.M.A ON")

def pInfo():
    pnAnswer = simpledialog.askstring("Add New Patient", "Insert Name")
    if pnAnswer is None:
       return
    paAnswer = simpledialog.askstring("Patient Age", "Insert Age") 
    pdAnswer = simpledialog.askstring("Patient's Illness", "Insert Illness (optional)") 
    pnoAnswer = simpledialog.askstring("Additional Notes", "Insert Notes (optional)") 
    L = ["Name of patient is: ", pnAnswer, "\n"]
    L2 = ["Age of patient: ", paAnswer, "\n"]
    L3 = ["Patient's Illness: ", pdAnswer,"\n" ]
    L4 = ["Notes: ", pnoAnswer,"\n" ] 
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file is None:
        return

    file.writelines(L + L2 + L3 + L4)
    file.close

    from tkinter import messagebox as mb
    res = mb.askquestion('Print', 
                         'Do you want to print the contents of the file to a Printer?')
      
    if res == 'yes' :
      import os
      os.startfile(file, "print")

    else :
        mb.showinfo('Return', 'Returning to main application')


def oInfo():
    """adds a new patient to the ui from saved files"""
    global CURRENT_LABEL_ROW 
    tf = filedialog.askopenfilename(title="Open Patient Information")
    tf = open(tf,"r")
    data = tf.read()
    Label(tkWindow, text=data, relief=FLAT).grid(row=CURRENT_LABEL_ROW, column=1, sticky=W)
    
    CURRENT_LABEL_ROW += 1 #increment the row position of the label by 1 so that the next label is added below the previous one
    

def closeWindow():
    tkWindow.quit()

# Button Creation


BTN = Button(tkWindow,
             text='New Patient ',
             #height=5,
             #width=10,
             command=pInfo)


BTN2 = Button(
tkWindow, 
text="Load Patient", 
#height=5,
#width=10,
command=oInfo
    )

BTN_QUIT = Button(tkWindow,
              text='Exit O.S.M.A',
              #height=5,
              #width=10,
              command=closeWindow)
 

# Placement
BTN.grid(column=0, row=0, sticky=W, padx=5, pady=5)
BTN2.grid(column=0, row=1,  sticky=W, padx=5, pady=5)
BTN_QUIT.grid(column=5, row=10,  sticky=W, padx=5, pady=450)

tkWindow.mainloop()