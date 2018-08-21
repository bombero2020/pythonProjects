# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:32:33 2018

@author: marce
"""

import pandas as pd

def nuevalista():
    '''Ojo solo hacerla una sola vez ya que crea una lista  nueva'''
    dias=list()
    gastos=list()
    for i in range(1,32):
        dias.append(i)
        gastos.append(0.)
    return dias,gastos
    
def nuevogasto():
    '''Crea un nuevo gasto en un día específico'''
    d=input("Introduce un día para añadir un gasto: ")
    g=input("Introduce un gasto para el día {}.".format(d))
    gastos[d]=g
    return gastos

data=pd.Series(gastos,index=dias,name="Gastos")
df=pd.DataFrame(data)


