from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog;




tkWindow = Tk()
tkWindow.geometry('800x600')
size = tkWindow['bg']='white'
tkWindow.title('O.S.M.A')



def pInfo():
    pnAnswer = simpledialog.askstring("Add New Patient", "Insert Name") 
    paAnswer = simpledialog.askstring("Patient Age", "Insert Age") 
    file1 = open("info.txt","w")
    L = ["Name of patient is: ", pnAnswer, "."]
    L2 = [
        " \nAge of patient: ", paAnswer, ".",]
    file1.writelines(L)
    file1.writelines(L2)
    file1.readable()
    


BTN = Button(tkWindow,
                text='Add New Patient',
             height=5,
             width=10,
             command=pInfo)

BTN.pack()
BTN.place(x=0, y=0)
    

def showMsg():
    file = open("info.txt","r")
    with open('info.txt') as f:
       data = file.read()
    messagebox.showinfo(data)


BTN2 = Button(tkWindow,
                text='Load Patient Info',
             height=5,
             width=10,
                command=showMsg)

BTN2.pack()
BTN2.place(x=0, y=125)

tkWindow.mainloop()