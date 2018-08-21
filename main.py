# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:58:42 2018

@author: marce
"""

import numpy as np
import pandas as pd

print("-"*60)
print("\tPrograma para manejar las cuentas de un restaurante")
print("-"*60)
numero_mesas=3

mesas=dict()
for i in range(numero_mesas):
    mesas[i+1]=0
    
#print(mesas)

#dict={"num_mesa":total}
mesa=int(input("Elija la mesa a modificar:\n"))
#print(mesa)
total=float(input("Importe: \n"))
mesas[mesa]=total
print("\t\tMesa {0}\n\t\tTotal:{1} €".format(mesa,mesas.get(mesa)))

#print(type(mesa))