import tkinter
from tkinter import *
root=tkinter.Tk()
root.geometry("1366x768+0+0")
root.title("Login Page")
mi=PhotoImage(file="Aman.gif")
L3=Label(root,image=mi,font=("arial",15),bg="black",fg="white")
L3.place(x=0,y=0)
E1=Entry(root,font=("Comic Sans MS",18),fg="green")
E1.place(x=725,y=245)
E2=Entry(root,font=("Comic Sans MS",18),fg="red",show="♥")
E2.place(x=725,y=350)
def axel():
    x=E1.get()
    y=E2.get()
    if x=="Axel":
        if y=="176044":
            messagebox.showinfo(message="Hello Axel!!",title="INFO!")
            import iot.py
    elif x=="SiD":
        if y=="176036":
            messagebox.showinfo(message="Hello SiD!!",title="INFO!")
    elif x=="Geetanshu":
        if y=="176070":
            messagebox.showinfo(message="Hello Geetanshu!!",title="INFO!")
    elif x=="Rajendra":
        if y=="176026":
            messagebox.showinfo(message="Hello Rajendra!!",title="INFO!")
    else:
        messagebox.showinfo(message="Invalid Username or Password!")
A1=Button(root,text="Log In",font=("Old English Text MT",24),fg="white",bg="indigo",command=axel)
A1.pack()
A1.place(x=650,y=500)

root.mainloop()
