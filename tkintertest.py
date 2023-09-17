import tkinter
from tkinter import messagebox
import os
 
window = tkinter.Tk()
 
window.title("Main Window")
 
# create a toplevel menu
menubar = tkinter.Menu(window)
helpmenu = tkinter.Menu(menubar)
 
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")
def login():
    inputtxt = tkinter.Text(window, height = 10,
                width = 25,
                bg = "light yellow")
 
def register():
    print("test")
    inputtxt = tkinter.Text(window, height = 10,
                width = 25,
                bg = "light yellow")
 
# display the menu
window.config(menu=menubar)
 
btn = tkinter.Button(window, 
                 text ="Login",
                 
                 command = lambda:login())
btn.pack(anchor='center')

 
btn2 = tkinter.Button(window, 
                 text ="Register",
                 
                 command = lambda:register())
btn2.pack(anchor='center')


 
window.mainloop()