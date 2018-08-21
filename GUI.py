# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:05:42 2018

@author: marce
"""
#Example (Hello, World): 
from tkinter import *

raiz=Tk()
raiz.geometry("500x250")

miframe=Frame(raiz,width=500,height=250)
miframe.pack()

cuadrotexto=Entry(miframe)
cuadrotexto.grid(row=0,column=1)

cuadrotexto1=Entry(miframe)
cuadrotexto1.grid(row=1,column=1)

cuadrotexto2=Entry(miframe)
cuadrotexto2.grid(row=2,column=1)

nombreLabel=Label(miframe,text="Nombre:")
nombreLabel.grid(row=0,column=0)

apellidoLabel=Label(miframe,text="Apellido:")
apellidoLabel.grid(row=1,column=0)

direccionLabel=Label(miframe,text="Direccion:")
direccionLabel.grid(row=2,column=0)

textoComent=Text(miframe,width=16,height=5)
textoComent.grid(row=4,column=1,padx=10,pady=10)

mibotton=Button(raiz,width=10,height=10)
mibotton.config()
raiz.mainloop()