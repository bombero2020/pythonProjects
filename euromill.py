# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:17:44 2018

@author: marcelo
"""

import numpy as np
import pandas as pd
import random as rd
import scipy.stats as ss
import matplotlib.pyplot as plt
from random import choices
 
from tkinter import *
from tkinter import ttk

print("\n\n----Inicio del análisis de los datos-----------\n\n")

def cargarDatos():
    '''Función para cargar los datos en un Dataframe'''
    datos=pd.read_csv("Resultados_base.csv",parse_dates=True)
    df=pd.DataFrame(datos)
    df.set_index('FECHA',inplace=True)
    return df
#%%
def actualizarLista():
    '''Función que toma todos los números, incluido el último, de los resultados 
        de los sorteos y los mete en Resultados_base.csv'''
    tabla=pd.read_html("https://docs.google.com/spreadsheet/pub?key=0AhqMeY8ZOrNKdEFUQ3VaTHVpU29UZ3l4emFQaVZub3c&amp"\
                       ,header=0,index_col=1)
    t=pd.DataFrame(tabla[0])
    
    t.drop(t.index[0],inplace=True,axis=0)     #quitamos la fila 0, ya que no hay datos
    t.drop(['1'],inplace=True,axis=1)   #quitamos la columna 1, no necesario
    t.drop(['Unnamed: 7'],inplace=True,axis=1) #quitamos la columna 7, no necesaria 
    enca=['N1','N2','N3','N4','N5','Star1','Star2']
    t.columns=enca                      #redefinimos las columnas
      #falta pasarlos a enteros
    t.to_csv('Resultados_base.csv')
    print("\nGuardado en Resultados_base.csv\n")    
#%%
###Guardamos ResultadosBackup.csv como backup de los datos y trabajamos con Resultados_base.csv
def guardarDatos(dataframe):
    '''Función para guardar los datos en un backup de respaldo'''
    dataframe.to_csv("ResultadosBackup.csv")
#%%    
df=cargarDatos()
last=df.head(1)
#print(df)
#%% Descripción de los datos
print("\n\n*****Descripción de los datos: *****\n")
#Mostrar las 10 primeras líneas del dataframe
df.head(10)
#Estadísticas
stat=df.describe()
print(stat)
#pd.plotting.scatter_matrix(df)
#Mediana: Deja el 50% de las muestras en la mitad
mediana=df.median()
print("Mediana: \n{}\n".format(df.median()))
#Moda #valor más repetido en frecuencia
moda=df.mode()
print("Moda: \n{}\n".format(moda))
#Media
media=df.mean()
print("Media: \n{}\n".format(media))
#Desviación Estándar 
std=df.std()
print("Desviación estándar: \n{}\n".format(df.std()))
#%%
n1=df.N1.values
n2=df.N2.values
n3=df.N3.values
n4=df.N4.values
n5=df.N5.values
st1=df.Star1.values
st2=df.Star2.values

#%% Necesito un método para ajustar la distribuvión de mis datos a una teorica
N1=df.N1.astype(int)

mediaN1, desviacionN1 = ss.norm.fit(N1)
 
print("media de N1: {}".format(mediaN1)) # media = 
print("desviación de N1: {}".format(desviacionN1)) # desviacion = 

#df.hist()
##https://blog.adrianistan.eu/2018/01/17/estadistica-python-ajustar-datos-una-distribucion-parte-vii/
#%%
def generarNumero():
    '''Funcion que genera un número aleatorio dentro del rango :
        [media-std,media+stf]'''
   #Nota: a veces da numeros repetidos en una jugada
    global media, std, mediana, moda
    limInf=round(media-std)
    limSup=round(media+std)
    numero=[]
    ls=[]
    for i in range(7):
        a=int(limInf[i])
        b=int(limSup[i])
        for j in range(a,b+1):
            ls.append(j)
        k=rd.choice(ls)
        ls=[]
        numero.append(k)
    return numero
    ############ 
#%%
def genNum():
    
    '''Funcion que genera un número aleatorio en funcion de los pesos'''
    global n1,n2,n3,n4,n5,st1,st2
    numero=[]
    for i in range(7):
        if (i==0):
            numero.append(choices(banda_n1,w_n1))
        elif(i==1):
            numero.append(choices(banda_n2,w_n2))
        elif(i==2):
            numero.append(choices(banda_n3,w_n3))
        elif(i==3):
            numero.append(choices(banda_n4,w_n4))
        elif(i==4):
            numero.append(choices(banda_n5,w_n5))
        elif(i==5):
            numero.append(choices(banda_st1,w_st1))
        elif(i==6):
            numero.append(choices(banda_st2,w_st2))
    return numero

#%%

population = [1, 2, 3, 4, 5, 6]
weights = [0.4, 0.2, 0.2, 0.1, 0.05, 0.05]    

banda_n1=[1,2,3,4,5,6,7,8,9,10]
w_n1=    [20,16,16,14,10,7,5,4,4,4]###weigths of the N1
banda_n2=[5, 6, 7, 8, 9,  10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
w_n2=    [3, 2, 4, 4, 3.5, 4, 5, 4, 5, 9, 18, 9, 5, 3, 4, 4, 3, 2.5, 3, 3, 2]
banda_n3=[20,21,22,23,24,25,26,27,28,29,30]
w_n3=    [8,8,7,8,10,15,15,10,7,6,6]
banda_n4=[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
w_n4=    [8,8,7,8,10,15,15,10,7,6,6]
banda_n5=[40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
w_n5=    [4,4,5,5,9,8,7,10,10,14,24]
banda_st1=[1,2,3,4,5,6]
w_st1=   [22,22,20,14,13,9]
banda_st2=[7,8,9,10,11,12]
w_st2=   [15,19,30,18,15,3]

choices(banda_n2, w_n2)
#%%    
pred=list()
def guardarPred(num):
    '''Guarda n números predichos en una bd o csv, usando generarNumero'''
    for i in range(1,num+1):
        #pred.append(generarNumero())
        pred.append(genNum())
    df=pd.DataFrame(pred)
    with open('Predictions.csv','a') as f:
        df.to_csv(f,header=False)    
    print(df) 
    
#%%
def calcfreq(numero):#numero debe ser N1.... Star1.. Star2
    '''Calcula la frecuencia de cada número 
        p,w=calcfreq(n) devuelve p:lista de numeros y w:pesos de cada uno'''
    l=len(numero)
    if max(numero)<=12:
        n=[i for i in range(1,13)]
    else:
        n=[i  for i in range(1,51) ]
    popu=[]
    weights=[]        
    for i in n:    
        count=0
        for j in numero:
            if i==j:
                count+=1
        w=100*(count/float(l))    
        #print(i,'encontrado',count,'times','weight',w)
        popu.append(i)
        weights.append(w)
        
    return (popu,weights)
   
    
#%% GUI
#class Aplicacion():
#    def __init__(self):
#        self.raiz = Tk()
#        self.raiz.geometry('600x400')
#        self.raiz.configure(bg = 'lightblue')
#        self.raiz.title('Euromillones')
#        self.etiq1=ttk.Label(self.raiz,text="Media")
#        self.etiq2=ttk.Label(self.raiz,text="Mediana")
#        self.etiq3=ttk.Label(self.raiz,text="Moda")
#        self.etiq4=ttk.Label(self.raiz,text="Desviacion estándar")
#        
#        
#        ttk.Label(self.raiz,text=numeros).pack(side="right")
#        ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy).pack(side="bottom")
#        
#        #CrearFrame(raiz)
#        self.raiz.mainloop()
#        
#def CrearFrame(raiz):
#    frame=Frame(raiz,width=300,height=200)
#    label1=ttk.Label(frame,text="Mediana")
#    label1.grid(row=2,column=1)
#
#def main():
#  mi_app = Aplicacion()
#  return 0
#
#if __name__ == '__main__':
#    main()