import cv2
import numpy as np
import matplotlib.pyplot as plt
#BORDES SIN LIBRERIA#
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
img = cv2.imread(ruta+"imagen_bordes.jpg")
img_gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
alto, ancho= img_gris.shape

kernel_suave = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])/9
suavizada = np.zeros((alto, ancho))
for i in range(1, alto -1):
    for j in range(1, ancho-1):
        suma = 0
        for ki in range(-1, 2):
            for kj in range(-1, 2):
                suma += img_gris[i+ki, j+kj] * kernel_suave[ki + 1, kj+1]
                suavizada[i,j] = suma
suavizada = suavizada.astype(np.uint8)

kernel = np.array([
    [1,1,1],
    [1,-8,1],
    [1,1,1]
])
bordes = np.zeros((alto, ancho))
for i in range(1, alto-1):
    for j in range(1, ancho-1):
        suma = 0
        for ki in range(-1,2):
            for kj in range(-1, 2):
                pixel = suavizada[i+ki, j+kj]
                peso = kernel[ki+1, kj+1]
                suma += pixel*peso
        bordes[i,j]= abs(suma)
        
bordes=bordes*2
bordes = np.clip(bordes, 0, 255)
bordes = bordes.astype(np.uint8)

boceto = np.zeros((alto, ancho), dtype=np.uint8)
umbral = 35
for i in range(alto):
    for j in range(ancho):
        if bordes[i,j]>umbral:
            boceto[i,j] = 0
        else:
            boceto[i,j] = 255
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(bordes, cmap="gray" )
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(boceto, cmap="gray" )
plt.axis("off")

plt.tight_layout()
plt.show()