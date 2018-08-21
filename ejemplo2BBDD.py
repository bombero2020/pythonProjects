# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:25:59 2018

@author: marce
"""

import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#miCursor.execute('''
#                 CREATE TABLE PRODUCTOS(
#                 CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#                 NOMBRE_ARTICULO VARCHAR(50),
#                 PRECIO INTEGER,
#                 SECCION VARCHAR(20))''')

productos=[("AR1","Jamones","19","Carniceria")]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",productos)

miConexion.commit()

miConexion.close()