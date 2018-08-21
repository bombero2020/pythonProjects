# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:22:33 2018

@author: marce
"""

import sqlite3 

miconexion=sqlite3.connect("MiPrimeraBasedeDAtos")

miCursor=miconexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

'''variosProductos=[
        ("Camiseta",10,"Deportes"),
        ("JArron",90,"Cerámica"),
        ("Camión",20,"Jugueteria"),

        ]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)'''

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for i in variosProductos:
    print(i[0])
    
    

miconexion.commit()

miconexion.close()
