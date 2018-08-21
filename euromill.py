# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:17:44 2018

@author: marcelo
"""

import numpy as np
import pandas as pd
import random as rd

from tkinter import *
from tkinter import ttk

print("\n\n----Inicio del análisis de los datos-----------\n\n")

datos=pd.read_csv("Resultados_base.csv")
df=pd.DataFrame(datos)
df.set_index('FECHA',inplace=True)
###Guardamos ResultadosBackup.csv como backup de los datos y trabajamos con Resultados_base.csv
datos.to_csv("ResultadosBackup.csv")

#print(df)
#%% Descripción de los datos
print("\n\n*****Descripción de los datos: *****\n")
#Mostrar las 10 primeras líneas del dataframe
df.head(10)
#Estadísticas
stat=df.describe()
print(stat)
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
#%% Necesito un método para ajustar la distribuvión de mis datos a una teorica

##https://blog.adrianistan.eu/2018/01/17/estadistica-python-ajustar-datos-una-distribucion-parte-vii/

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
        

#%%
def generarNumero():
    '''Funcion que genera un número aleatorio dentro del rango :
        [mediana-std,mediana+stf]'''
   
    global media, std
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