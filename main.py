from os import stat
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile


# Initial window setup
tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg'] = 'white'
tkWindow.resizable(False, False)
tkWindow.title('O.S.M.A')


# Function Definitions

active = print("O.S.M.A ON")


def pInfo():
    pnAnswer = simpledialog.askstring("Add New Patient", "Insert Name")
    paAnswer = simpledialog.askstring("Patient Age", "Insert Age") 
    pdAnswer = simpledialog.askstring("Patient's Illness", "Insert Illness (optional)") 
    pnoAnswer = simpledialog.askstring("Additional Notes", "Insert Notes (optional)") 
    L = ["Name of patient is: ", pnAnswer, "\n"]
    L2 = ["Age of patient: ", paAnswer, "\n"]
    L3 = ["Patient's Illness: ", pdAnswer,"\n" ]
    L4 = ["Notes: ", pnoAnswer,"\n" ] 
    file = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    if file is None:
        return

    file.writelines(L + L2 + L3)
    file.close


def oInfo():
    tf = filedialog.askopenfilename(title="Open Patient Information")
    tf = open(tf)
    data = tf.read()
    Label(tkWindow, text=data, relief=FLAT)
 

def closeWindow():
    tkWindow.destroy()


# Button Creation


BTN = Button(tkWindow,
             text='Add New Patient',
             #height=5,
             #width=10,
             command=pInfo)


BTN2 = Button(
tkWindow, 
text="Load Patient Info", 
#height=5,
#width=10,
command=oInfo
    )


BTN_QUIT = Button(tkWindow,
              text='Exit O.S.M.A',
              #height=5,
              #width=10,
              command=closeWindow)
 



# Packing
BTN.pack()
BTN_QUIT.pack()


# TODO: I highly recommend switching to a grid layout, easier to control where elements are :)
# Placement
BTN.place(x=0, y=0)
BTN2.place(x=0, y=75)
BTN_QUIT.place(x=625, y=500)


# Run the window
tkWindow.mainloop()


