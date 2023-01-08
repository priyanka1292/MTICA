from tkinter import *
master=Tk()
#Label(master,text="first name").grid(row=0)
l1=Label(master,text="first name")
l1.grid(row=0,column=0)
#Label(master,text="first name").grid(row=1)
l2=Label(master,text="last name")
l2.grid(row=1,column=0)

e1=Entry(master)
e2=Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()

