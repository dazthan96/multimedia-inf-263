import cv2
import numpy as np
import matplotlib.pyplot as plt
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
cuerpo_monigote = cv2.imread(ruta+"mono.png")
cabeza_payaso = cv2.imread(ruta+"cabeza_payaso.png")
original = cuerpo_monigote.copy()
y1,y2= 90,430
x1,x2= 220,590
alto = y2-y1
ancho = x2=x1
cabeza_payaso=cv2.resize(cabeza_payaso, (alto, ancho))
cuerpo_monigote[y1:y2, x1:x2]=cabeza_payaso
cv2.imwrite(ruta+"final.png",cuerpo_monigote)
plt.show()