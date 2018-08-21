# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:51:57 2018

@author: marce
"""

#capturar

import cv2
# Camara 1 es la camara web integrada en mi caso
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 1
#iniciar camara
camera = cv2.VideoCapture(camara)
# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in range(fotogramas):
 temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
camera_capture = get_image()
file = "captura.png"
# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, camera_capture)
# finalizar camara
del(camera)