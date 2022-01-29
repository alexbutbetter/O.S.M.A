from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


# Initial window setup
tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg'] = 'white'
tkWindow.title('O.S.M.A')


# Function Definitions
def pInfo():
    pnAnswer = simpledialog.askstring("Add New Patient", "Insert Name")
    paAnswer = simpledialog.askinteger("Patient Age", "Insert Age") # Changed this to askinteger
    file1 = open("info.txt", "a")
    L = ["Name of patient is: ", pnAnswer, "\n"]
    L2 = ["Age of patient: ", paAnswer, "\n"]
    file1.writelines(L + L2)

    # readable simply returns true or false just fyi
    file1.readable()


def showMsg():
    # Redundant to open it twice
    # file = open("info.txt", "r")
    with open('info.txt') as f:
        # You open it as f so you call f.read
        data = f.read()
    # You have to specify the arguments if you are using anything past the first
    # The first argument that showinfo takes in is the title, so it assumed title=data
    messagebox.showinfo(title="Patient Info", message=data)


def closeWindow():
    tkWindow.destroy()


# Button Creation
BTN = Button(tkWindow,
             text='Add New Patient',
             # height=5,
             # width=10,
             command=pInfo)


BTN2 = Button(tkWindow,
              text='Load Patient Info',
              # height=5,
              # width=10,
              command=showMsg)

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
