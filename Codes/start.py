# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:29:43 2020

@author: Axel Blaze
"""
import tkinter
from tkinter import *
def login():
    if uname.get()=="" or pas.get()=="":
        messagebox.showerror("Error","All Fields Required..!!")
    elif uname.get()=="Axel" and pas.get()=="40440Axel":
        messagebox.showinfo("Successful",f"Welcome {uname.get()}")
        
        
    elif uname.get()=="Antra":
        messagebox.showinfo("Welcome Madam","At Your Service Mam ♥♥♥")
        messagebox.showinfo("Welcome Madam","Welcome Ms Antra ☻")
        
    else:
        messagebox.showerror("Error","Invalid Username or Password")
root=tkinter.Tk()
root.title("Detection Of Depression")
root.geometry("1366x768+0+0")
uname=StringVar()
pas=StringVar()
bg_icon=PhotoImage(file="MDD6.png")
user_icon=PhotoImage(file="user.png")
password_icon=PhotoImage(file="pass.png")
logo_icon=PhotoImage(file="logo.png")
bg_lbl=Label(root,image=bg_icon).pack()
title=Label(root,text="Login Portal",font=("lucida calligraphy",40,"bold"),bg="#213970",fg="#F49F1C",bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)
Login=Frame(root,bg='white')
Login.place(x=450, y=200) 
logolbl=Label(Login,image=logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
lbluser=Label(Login,text="Username:",image=user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
lblpassword=Label(Login,text=" Password:",image=password_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
tuser=Entry(Login,bd=5,textvariable=uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
tpassword=Entry(Login,bd=5,textvariable=pas,relief=GROOVE,font=("",15),fg="red",show="♥").grid(row=2,column=1,padx=20)
btn_log=Button(Login,text="Login",width=5,height=1,font=("lucida calligraphy",14,"bold"),bg="#213970",fg="#F49F1C",command=login).grid(row=3,columnspan=2,pady=10)
root.mainloop()
