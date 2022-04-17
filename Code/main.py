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
from turtle import exitonclick

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

def help():
    from tkinter import messagebox as mb
    mb.showinfo('Error Codes in O.S.M.A', 'Error 1 - To be made / unfinished function, Error 2 - No data in value, Error 3 - Placeholder, Error 4 - Incorrect file extension')


menubar = Menu(tkWindow)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)


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
                         'Do you want to print the contents of the file to a Printer? (to be made)')
      
    if res == 'yes' :
      mb.showerror('ERROR 1', 'ERROR 1 (check wiki for more info)')

    else :
        mb.showinfo('Return', 'Returning to main application')


def oInfo():
    """adds a new patient to the ui from saved files"""
    global CURRENT_LABEL_ROW 
    tf = filedialog.askopenfilename(title="Open Patient Information")
    import os 
    file_extension = os.path.splitext(tf)[1]
    if file_extension.lower() == ".txt":
        None
    else:
        from tkinter import messagebox as mb 
        mb.showerror('ERROR 4', 'Error 4, check wiki and Help tab for more information')

    tf = open(tf,"r")

    data = tf.read()
    Label(tkWindow, text=data, relief=FLAT).grid(row=3, column=2)
    
    

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
BTN_QUIT.grid(column=5, row=30, padx=5, pady=400)

tkWindow.config(menu=menubar)

tkWindow.mainloop()