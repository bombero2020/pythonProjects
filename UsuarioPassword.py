# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:27:21 2018

@author: marce
"""

from tkinter import *

usr="Marcelo"
passw="123"
msg=""

raiz=Tk()
raiz.geometry("300x200")

miframe=Frame(raiz,width=800,height=800,bg="blue")
miframe.pack()

def comprobarClave():
    user=cuadrotexto.get()
    if user==usr:
        msg="Usuario correcto"
        print("Usuario correcto")
    else:
        msg="Usuario incorrecto"
        
nombreLabel=Label(miframe,text="Usuario:")
nombreLabel.grid(row=0,column=0)

cuadrotexto=Entry(miframe)
cuadrotexto.grid(row=0,column=1)

apellidoLabel=Label(miframe,text="Password:")
apellidoLabel.grid(row=1,column=0)

cuadrotexto1=Entry(miframe)
cuadrotexto1.grid(row=1,column=1)

mensajeLabel=Label(miframe,text=msg)
mensajeLabel.grid(row=3,column=0)

def callback():
    print("click")

mibotton=Button(raiz,width=5,height=2,text="Enviar",command=comprobarClave)
mibotton.pack()
mibotton.config(relief=RAISED)


raiz.mainloop()