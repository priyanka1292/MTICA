from tkinter import *
import math
root=Tk()
root.title("calculator")
e=Entry(root)
e.grid(row=0,column=0,columnspan=6)
e.focus_set()

def clearall():
    e.delete(0,END)
def clear1():
    txt=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)
def fund7():
    txt=e.get()
