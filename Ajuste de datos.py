# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:59:58 2018

@author: marce
"""
import pandas as pd
import scipy.stats as ss
 
df = pd.read_csv("alturas.csv")
 
media, desviacion = ss.norm.fit(df["Altura"])
 
print("media: {}".format(media)) # media = 160,37
print("desviación: {}".format(desviacion)) # desviacion = 17,41

#df.hist()

#%% Ajuste Kolmogorov
d, pvalor = ss.ktest(df["Altura"],"norm",args=(media,desviacion))
print("d: {}".format(d))
print("p valor: {}".format(p))
# o alternativamente
#d, pvalor = ss.ktest(df["Altura"],lambda x: ss.norm.cdf(x,media,desviacion))

#%%
