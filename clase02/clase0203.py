import cv2
import matplotlib.pyplot as plt
#BORDES CON LIBRERIA#
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
img = cv2.imread(ruta+"bordes_imagen.webp")
bordes = cv2.Canny(img, 100, 200)
plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(bordes, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()