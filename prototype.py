#operating system

#Imports
import os
import sys
from tkinter import *
from func import *

#GUI Setup
root = Tk()
root.title("Operating System Prototype")
root.geometry("1000x750")
root.resizable(True, True)
root.configure(background="black")

#Clock Handler
time = Label(
    root,
    text=clock_time(),
    foreground="green",
    background="black",
    width = 10, 
    height = 2, 
)
date = Label(
    root,
    text=clock_date(),
    foreground="green",
    background="black",
    width = 10,
    height = 2
)

#Welcome Message
welcome_message = Label(
    root, 
    text="This is a prototype of an operating system", 
    foreground="green",
    background="black",
    width = 100,
    height = 100
)

#Packing System
time.pack(anchor="ne")
date.pack(anchor="n")
welcome_message.pack(anchor="center")
root.mainloop()