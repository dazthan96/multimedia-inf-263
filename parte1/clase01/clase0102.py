import cv2
import numpy as np
import matplotlib.pyplot as plt
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
payaso = cv2.imread(ruta+"payaso.jpeg")
#PARA EL MONIGOTE
y1, y2 = 10, 265
x1,x2 = 100, 450
cabeza_payaso = payaso[y1:y2, x1:x2]
#PARA GUARDAR IMAGENES
cv2.imwrite(ruta+"cabeza_payaso.png", cabeza_payaso)
# 1. Crear la cuadrícula (1 fila, 2 columnas)
# figsize=(10, 5) define el ancho y alto de la ventana en pulgadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(cv2.cvtColor(payaso, cv2.COLOR_BGR2RGB))
ax1.set_title("payaso entero")

ax2.imshow(cv2.cvtColor(cabeza_payaso, cv2.COLOR_BGR2RGB))
ax2.set_title("cabeza payaso")
ax2.axis("off") 
#hasta aqui
#PARA EL PAYASO
plt.tight_layout()
plt.show()