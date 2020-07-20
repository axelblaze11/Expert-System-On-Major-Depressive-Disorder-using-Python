# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:10:53 2020

@author: Axel Blaze
"""
import tkinter
from tkinter import *
import numpy as np
import pandas as pd
import os
from sklearn import model_selection
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
df=pd.read_excel(r'source.xlsx')
X_train=df.iloc[:,0:19]
y_train=df.iloc[:,19]
model = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(base_estimator=model, n_estimators=num_trees, random_state=0)
model.fit(X_train,y_train)
def test():
    ch=[]
    ar=[]
    i1=v1.get()
    ch.append(i1)
    i2=v2.get()
    ch.append(i2)
    i3=v3.get()
    ch.append(i3)
    i4=v4.get()
    ch.append(i4)
    i5=v5.get()
    ch.append(i5)
    i6=v6.get()
    ch.append(i6)
    i7=v7.get()
    ch.append(i7)
    i8=v8.get()
    ch.append(i8)
    i9=v9.get()
    ch.append(i9)
    i10=v10.get()
    ch.append(i10)
    i11=v11.get()
    ch.append(i11)
    i12=v12.get()
    ch.append(i12)
    i13=v13.get()
    ch.append(i13)
    i14=v14.get()
    ch.append(i14)
    i15=v15.get()
    ch.append(i15)
    i16=v16.get()
    ch.append(i16)
    i17=v17.get()
    ch.append(i17)
    i18=v18.get()
    ch.append(i18)
    i19=v19.get()
    ch.append(i19)   
    ar=pd.DataFrame(ch)   
    ar.to_csv(r'test.csv',index=False)
    t=pd.read_csv(r'test.csv')
    x=t.iloc[0:19,0]
    X_test=np.vstack((x,x))
    y_pred = model.predict(X_test)
    os.remove(r'test.csv')
    if y_pred[0]==0:
        l20=Label(Login,text="Result:",font=("times new roman",12,"bold"),bg="cyan").grid(row=20,column=0,padx=20)        
        r=Entry(Login,bd=5,textvariable=v20,relief=GROOVE,font=("times new roman",12),fg="green").grid(row=20,column=1,padx=20) #19    
        v20.set("It's Normal")
        l20.destroy()
        r.destroy()
        
    else:
        l20=Label(Login,text="Result:",font=("times new roman",12,"bold"),bg="cyan").grid(row=20,column=0,padx=20)        
        r=Entry(Login,bd=5,textvariable=v20,relief=GROOVE,font=("times new roman",12),fg="red").grid(row=20,column=1,padx=20) #19    
        v20.set("Depression Detected")
        messagebox.showinfo(message="Depression Detected",title="Result")
        
  
def demo():
    v1.set("1") 
    v2.set("0.000161")
    v3.set("0.00000154")
    v4.set("0.00359")
    v5.set("0.00276")
    v6.set("0.9963")
    v7.set("0.00347")
    v8.set("0.9963")
    v9.set("0.9291")
    v10.set("0.9918")
    v11.set("0.9990")
    v12.set("0.0038")
    v13.set("0.0002")
    v14.set("0.0060")
    v15.set("0.0185")
    v16.set("0.9808")
    v17.set("0.0190")
    v18.set("0.980852")
    v19.set("0.5298")
    
def reset():
    v1.set("") 
    v2.set("")
    v3.set("")
    v4.set("")
    v5.set("")
    v6.set("")
    v7.set("")
    v8.set("")
    v9.set("")
    v10.set("")
    v11.set("")
    v12.set("")
    v13.set("")
    v14.set("")
    v15.set("")
    v16.set("")
    v17.set("")
    v18.set("")
    v19.set("")
    v20.set("")

def demo2():
    v1.set("0.821576") 
    v2.set("0.249583")
    v3.set("0.00000289")
    v4.set("0.023302")
    v5.set("0.226832")
    v6.set("0.784104")
    v7.set("0.215857")
    v8.set("0.78406")
    v9.set("0.929139")
    v10.set("0.998472")
    v11.set("0.840509")
    v12.set("0.22268")
    v13.set("0.00000293")
    v14.set("0.055637")
    v15.set("0.297828")
    v16.set("0.704763")
    v17.set("0.295206")
    v18.set("0.704763")
    v19.set("0.526313")
    v20.set("")
root=Tk()
root.geometry("1160x774")
root.title("Detect of MDD using Signal Data")
root.resizable(0,0)
back=PhotoImage(file="signal.png")
v1=StringVar() 
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
v10=StringVar()
v11=StringVar()
v12=StringVar()
v13=StringVar()
v14=StringVar()
v15=StringVar()
v16=StringVar()
v17=StringVar()
v18=StringVar()
v19=StringVar()  
v20=StringVar()  
v21=StringVar()
title=Label(root,text="                                  Detection Of MDD Using Signals                                ",font=("lucida calligraphy",20,"bold"),bg="#213970",fg="#F49F1C",bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=2)
L=Label(root,image=back,font=("arial",15))
Login=Frame(root,bg='cyan')
Login.place(x=400, y=70)
l1=Label(Login,text="Channel 1:",font=("times new roman",12,"bold"),bg="cyan").grid(row=1,column=0,padx=20)
l2=Label(Login,text="Channel 2:",font=("times new roman",12,"bold"),bg="cyan").grid(row=2,column=0,padx=20)
l3=Label(Login,text="Channel 3:",font=("times new roman",12,"bold"),bg="cyan").grid(row=3,column=0,padx=20)
l4=Label(Login,text="Channel 4:",font=("times new roman",12,"bold"),bg="cyan").grid(row=4,column=0,padx=20)
l5=Label(Login,text="Channel 5:",font=("times new roman",12,"bold"),bg="cyan").grid(row=5,column=0,padx=20)
l6=Label(Login,text="Channel 6:",font=("times new roman",12,"bold"),bg="cyan").grid(row=6,column=0,padx=20)
l7=Label(Login,text="Channel 7:",font=("times new roman",12,"bold"),bg="cyan").grid(row=7,column=0,padx=20)
l8=Label(Login,text="Channel 8:",font=("times new roman",12,"bold"),bg="cyan").grid(row=8,column=0,padx=20)
l9=Label(Login,text="Channel 9:",font=("times new roman",12,"bold"),bg="cyan").grid(row=9,column=0,padx=20)
l10=Label(Login,text="Channel 10:",font=("times new roman",12,"bold"),bg="cyan").grid(row=10,column=0,padx=20)
l11=Label(Login,text="Channel 11:",font=("times new roman",12,"bold"),bg="cyan").grid(row=11,column=0,padx=20)
l12=Label(Login,text="Channel 12:",font=("times new roman",12,"bold"),bg="cyan").grid(row=12,column=0,padx=20)
l13=Label(Login,text="Channel 13:",font=("times new roman",12,"bold"),bg="cyan").grid(row=13,column=0,padx=20)
l14=Label(Login,text="Channel 14:",font=("times new roman",12,"bold"),bg="cyan").grid(row=14,column=0,padx=20)
l15=Label(Login,text="Channel 15:",font=("times new roman",12,"bold"),bg="cyan").grid(row=15,column=0,padx=20)
l16=Label(Login,text="Channel 16:",font=("times new roman",12,"bold"),bg="cyan").grid(row=16,column=0,padx=20)
l17=Label(Login,text="Channel 17:",font=("times new roman",12,"bold"),bg="cyan").grid(row=17,column=0,padx=20)
l18=Label(Login,text="Channel 18:",font=("times new roman",12,"bold"),bg="cyan").grid(row=18,column=0,padx=20)
l19=Label(Login,text="Channel 19:",font=("times new roman",12,"bold"),bg="cyan").grid(row=19,column=0,padx=20)

c1=Entry(Login,bd=5,textvariable=v1,relief=GROOVE,font=("times new roman",12)).grid(row=1,column=1,padx=20) #1
c2=Entry(Login,bd=5,textvariable=v2,relief=GROOVE,font=("times new roman",12)).grid(row=2,column=1,padx=20) #2 
c3=Entry(Login,bd=5,textvariable=v3,relief=GROOVE,font=("times new roman",12)).grid(row=3,column=1,padx=20) #3
c4=Entry(Login,bd=5,textvariable=v4,relief=GROOVE,font=("times new roman",12)).grid(row=4,column=1,padx=20) #4
c5=Entry(Login,bd=5,textvariable=v5,relief=GROOVE,font=("times new roman",12)).grid(row=5,column=1,padx=20) #5
c6=Entry(Login,bd=5,textvariable=v6,relief=GROOVE,font=("times new roman",12)).grid(row=6,column=1,padx=20) #6
c7=Entry(Login,bd=5,textvariable=v7,relief=GROOVE,font=("times new roman",12)).grid(row=7,column=1,padx=20) #7
c8=Entry(Login,bd=5,textvariable=v8,relief=GROOVE,font=("times new roman",12)).grid(row=8,column=1,padx=20) #8
c9=Entry(Login,bd=5,textvariable=v9,relief=GROOVE,font=("times new roman",12)).grid(row=9,column=1,padx=20) #9
c10=Entry(Login,bd=5,textvariable=v10,relief=GROOVE,font=("times new roman",12)).grid(row=10,column=1,padx=20) #10
c11=Entry(Login,bd=5,textvariable=v11,relief=GROOVE,font=("times new roman",12)).grid(row=11,column=1,padx=20) #11
c12=Entry(Login,bd=5,textvariable=v12,relief=GROOVE,font=("times new roman",12)).grid(row=12,column=1,padx=20) #12
c13=Entry(Login,bd=5,textvariable=v13,relief=GROOVE,font=("times new roman",12)).grid(row=13,column=1,padx=20) #13
c14=Entry(Login,bd=5,textvariable=v14,relief=GROOVE,font=("times new roman",12)).grid(row=14,column=1,padx=20) #14
c15=Entry(Login,bd=5,textvariable=v15,relief=GROOVE,font=("times new roman",12)).grid(row=15,column=1,padx=20) #15
c16=Entry(Login,bd=5,textvariable=v16,relief=GROOVE,font=("times new roman",12)).grid(row=16,column=1,padx=20) #16
c17=Entry(Login,bd=5,textvariable=v17,relief=GROOVE,font=("times new roman",12)).grid(row=17,column=1,padx=20) #17
c18=Entry(Login,bd=5,textvariable=v18,relief=GROOVE,font=("times new roman",12)).grid(row=18,column=1,padx=20) #18
c19=Entry(Login,bd=5,textvariable=v19,relief=GROOVE,font=("times new roman",12)).grid(row=19,column=1,padx=20) #19

#r=Entry(Login,bd=5,textvariable=v21,relief=GROOVE,font=("times new roman",12),fg="red",state=DISABLED).grid(row=20,column=1,padx=20) #19
B2=Button(root,text="Click for results",font=("Lucida Calligraphy",14),fg="white",bg="purple",relief=GROOVE,command=test)
B2.pack()
B2.place(x=877,y=183)
B3=Button(root,text="Reset",font=("Bodoni MT",14),fg="white",bg="purple",relief=GROOVE,command=reset)
B3.pack()
B3.place(x=935,y=600)
B4=Button(root,text="Click Here For\n Demo Values",font=("Bodoni MT",14),fg="white",bg="purple",relief=GROOVE,command=demo)
B4.pack()
B4.place(x=900,y=525)
#B5=Button(root,text="Click Here For\n Demo Values",font=("Bodoni MT",14),fg="white",bg="purple",relief=GROOVE,command=demo2)
#B5.pack()
lblRules = Label(
    root,
    text = "The System predicts whether a person\n is suffering from Depression or not\n by using the signal data of 19 channels.\n This system is trained under theta band \npower which has the frequency of 4-8Hz.\n You just have to enter the signal data of\n all 19 channels in theta band power and\n click on the results  ",
    width = 35,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()
lblRules.place(x=775,y=300)
title.pack()
L.pack()

root.mainloop()
