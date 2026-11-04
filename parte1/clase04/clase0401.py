import cv2
import matplotlib.pyplot as plt

ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/"
ninio = cv2.imread(ruta + "ninio.jpg")

gris = cv2.cvtColor(ninio, cv2.COLOR_BGR2GRAY)#convierte la imagen leida en una escala de grises de un solo canal
bordes = cv2.Canny(gris, 100, 200)#canny detecta los bordes
resultado = ninio.copy()#realiza una copia para que no afecte a la imgen orginal

resultado[bordes>0]=[255,0,0]#colorea los bordes detectados de color azul


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(ninio, cv2.COLOR_BGR2RGB))
plt.title("imagen original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("imagen bordes remarcados")
plt.axis("off")

plt.tight_layout()
plt.show()