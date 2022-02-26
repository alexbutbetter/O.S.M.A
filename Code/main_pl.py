# O.S.M.A by Aleksander Kurpiewski

from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import main
import os 

#Global varible to store the row poition of the label
CURRENT_LABEL_ROW =0

# Initial window setup
tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg'] = 'white'
s = ttk.Style()
tkWindow.tk.call("source", "azure.tcl")
tkWindow.tk.call("set_theme", "dark")
tkWindow.title('O.S.M.A (Polski)')



# configure the grid columns and weights
tkWindow.columnconfigure(0, weight=1)
tkWindow.columnconfigure(1, weight=3)


# Function Definitions

active = print("O.S.M.A ON")


def pInfo():
    pnAnswer = simpledialog.askstring("Dodaj nowego pacjenta", "Wprowadź imię pacjenta")
    paAnswer = simpledialog.askstring("Wiek pacjenta", "Wprowadź wiek pacjenta") 
    pdAnswer = simpledialog.askstring("Wprowadź chorobę pacjenta", "Wyprowdź chorobę (dodatkowę)") 
    pnoAnswer = simpledialog.askstring("Notatki dodatkowę", "Wyprowadż notatkę (dodatkowę)") 
    L = ["Imię pacjenta: ", pnAnswer, "\n"]
    L2 = ["Wiek pacjenta: ", paAnswer, "\n"]
    L3 = ["Choroba Pacjenta: ", pdAnswer,"\n" ]
    L4 = ["Notatki: ", pnoAnswer,"\n" ] 
    file = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    if file is None:
        return

    file.writelines(L + L2 + L3 + L4)
    file.close


def oInfo():
    """adds a new patient to the ui from saved files"""
    global CURRENT_LABEL_ROW 
    tf = filedialog.askopenfilename(title="Wybierz pacjenta")
    tf = open(tf,"r")
    data = tf.read()
    Label(tkWindow, text=data, relief=FLAT).grid(row=CURRENT_LABEL_ROW, column=1, sticky=W)
    
    CURRENT_LABEL_ROW += 1 #increment the row position of the label by 1 so that the next label is added below the previous one
    

def closeWindow():
    tkWindow.quit()





# Button Creation


BTN = Button(tkWindow,
             text='Dodaj nowego pacjenta ',
             #height=5,
             #width=10,
             command=pInfo)


BTN2 = Button(
tkWindow, 
text="Otwórz danę pacjenta", 
#height=5,
#width=10,
command=oInfo
    )


BTN_QUIT = Button(tkWindow,
              text='Exit O.S.M.A',
              #height=5,
              #width=10,
              command=closeWindow)
 





# TODO: I highly recommend switching to a grid layout, easier to control where elements are :)
# Placement
BTN.grid(column=0, row=0, sticky=W, padx=5, pady=5)
BTN2.grid(column=0, row=1,  sticky=W, padx=5, pady=5)
BTN_QUIT.grid(column=5, row=10,  sticky=W, padx=5, pady=450)

tkWindow.mainloop()