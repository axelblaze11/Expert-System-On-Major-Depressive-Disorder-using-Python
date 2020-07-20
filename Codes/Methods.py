# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:53:06 2020
@author: Axel Blaze
"""
import tkinter
from tkinter import *
from tkinter.font import Font


def b():
    root.destroy()
    import bdi
def h():
    root.destroy()
    import HAM_D
def d():
    root.destroy()
    import DSM_5
def s():
    root.destroy()
    import Signals

root=tkinter.Tk()
my_font = Font(family="Lucida Calligraphy", size=40, weight="bold")
my_font1 = Font(family="Lucida Calligraphy", size=16)
root.geometry("1366x768+0+0")
root.title("Testing Methods")
back=PhotoImage(file="MDD3.png")
L=Label(root,image=back,font=(my_font),bg="#213970",fg="#F49F1C")
t=Label(root,text="            Methods For Detecting Depression         ",font=my_font,bg="#213970",fg="#F49F1C",bd=10)
t.place(x=0,y=0)
B1=Button(root,text="Hamilton Depression Rating Scale \n (HAM-D)",font=my_font1,fg="white",bg="#7DB46C",command=h)
B1.pack()
B2=Button(root,text="Depression DSM-5 Diagonistic Criteria",font=my_font1,fg="white",bg="#7DB46C",command=d)
B2.pack()
B3=Button(root,text="Beck's Depression Inventory \n (BDI)",font=my_font1,fg="white",bg="#7DB46C",command=b)
B3.pack()
B4=Button(root,text="Detection of MDD using Signals",font=("Lucida Calligraphy",16),fg="white",bg="#7DB46C",command=s)
B4.pack()
B1.place(x=500,y=250)
B2.place(x=475,y=175)
B3.place(x=535,y=340)
B4.place(x=515,y=435)
t.pack()
L.pack()
root.mainloop()

