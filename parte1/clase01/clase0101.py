import cv2
import numpy as np
import matplotlib.pyplot as plt
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
mono = cv2.imread(ruta+"mono.png")
#PARA EL MONIGOTE
y1, y2 = 90, 430
x1,x2 = 220, 590
cabeza_mono = mono[y1:y2, x1:x2]
# 1. Crear la cuadrícula (1 fila, 2 columnas)
# figsize=(10, 5) define el ancho y alto de la ventana en pulgadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(cv2.cvtColor(mono, cv2.COLOR_BGR2RGB))
ax1.set_title("monigote entero")

ax2.imshow(cv2.cvtColor(cabeza_mono, cv2.COLOR_BGR2RGB))
ax2.set_title("cabeza monigote")
ax2.axis("off")
plt.tight_layout()
plt.show()