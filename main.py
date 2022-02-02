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



       

def pInfo():
    pnAnswer = simpledialog.askstring("Add New Patient", "Insert Name")
    paAnswer = simpledialog.askstring("Patient Age", "Insert Age") # Changed this to askinteger and now i changed it to askstring cuz uhh idfk
    pdAnswer = simpledialog.askstring("Patient's Illness", "Insert Illness (optional)") 
    
    L = ["Name of patient is: ", pnAnswer, "\n"]
    L2 = ["Age of patient: ", paAnswer, "\n"]
    L3 = ["Patient's Illness: ", pdAnswer,"\n" ]

    file = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    if file is None:
        return

    file.writelines(L + L2 + L3)
    file.close


def open():
    file = askopenfile(mode='r')
    messagebox.showinfo(file.readlines())


def closeWindow():
    tkWindow.destroy()


# Button Creation

text = Tk.Text(tkWindow, height=12)
text.grid(column=0, row=0, sticky='nsew')

BTN = Button(tkWindow,
             text='Add New Patient',
             # height=5,
             # width=10,
             command=pInfo)


BTN2 = Button(tkWindow,
              text='Load Patient Info',
              # height=5,
              # width=10,
              command=open)

BTN_QUIT = Button(tkWindow, text="Quit", command=closeWindow)


# Packing
BTN.pack()
BTN2.pack()
BTN_QUIT.pack()

# TODO: I highly recommend switching to a grid layout, easier to control where elements are :)
# Placement
BTN.place(x=0, y=0)
BTN2.place(x=0, y=125)
BTN_QUIT.place(x=700, y=500)

# Run the window
tkWindow.mainloop()


