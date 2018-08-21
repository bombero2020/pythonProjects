# -*- coding: utf-8 -*-
"""
Created on Tue May 15 01:13:19 2018

@author: marce
"""

from tkinter import *

raiz=Tk()

miframe=Frame(raiz,width=800,height=800)

miframe.pack()

operacion=""

reset_pantalla=False

resultado=0

#milabel=Label(miframe,text="Hola Amigos",fg="red",font=(18"))
#milabel.pack()

#----------------pantalla----------------#
numeroPantalla=StringVar()
pantalla=Entry(miframe, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background='black',fg='white',justify='right')

#------Pulsaciones de teclado------------#
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    numeroPantalla.set(numeroPantalla.get()+num)
   
#----------------funcion suma----------------------------------

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	resultado+=int(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)

#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0

    
#----------------fila 1 ------------------#

boton7=Button(miframe,text='7',width=3,command=numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miframe,text='8',width=3,command=numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miframe,text='9',width=3,command=numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonX=Button(miframe,text='X',width=3)
botonX.grid(row=2,column=4)

#----------------fila 2 ------------------#

boton4=Button(miframe,text='4',width=3,command=numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miframe,text='5',width=3,command=numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miframe,text='6',width=3,command=numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonDiv=Button(miframe,text='/',width=3)
botonDiv.grid(row=3,column=4)

#----------------fila 3 ------------------#

boton1=Button(miframe,text='1',width=3,command=numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miframe,text='2',width=3,command=numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miframe,text='3',width=3,command=numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonMenos=Button(miframe,text='-',width=3)
botonMenos.grid(row=4,column=4)

#----------------fila 4 ------------------#

botonPunto=Button(miframe,text='.',width=3)
botonPunto.grid(row=5,column=1)
boton0=Button(miframe,text='0',width=3,command=numeroPulsado("0"))
boton0.grid(row=5,column=2)
botonIgual=Button(miframe,text='=',width=3)
botonIgual.grid(row=5,column=3)
botonMas=Button(miframe,text='+',width=3)
botonMas.grid(row=5,column=4)

#---------------Texto en fila 7 -----------#
label=Label(miframe,text="Calculadora")
label.grid(row=6,column=1,padx=10,pady=10,columnspan=4)
#---------------Imagen en fila 8 ----------#

#miImagen=PhotoImage(file="donut.gif")
#miImagen.

raiz.mainloop()