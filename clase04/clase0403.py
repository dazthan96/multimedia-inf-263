import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/ninio.jpg")
gris = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
suavizado = cv2.bilateralFilter(gris, 9,75,75)
bordes = cv2.Canny(suavizado, 30,100)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
bordes_cerrados = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, kernel)

contornos, _ = cv2.findContours(bordes_cerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mascara = np.zeros(gris.shape, dtype=np.uint8)

if contornos:
    contorno_mayor = max(contornos, key=cv2.contourArea)
    cv2.drawContours(mascara, [contorno_mayor], -1, 255, -1)
fondo = np.zeros_like(img)
fondo[:]=[255,0,0]

resultado = img.copy()
resultado[mascara==0] = fondo[mascara==0]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("bordes")
plt.axis("off")

plt.tight_layout()
plt.show()
