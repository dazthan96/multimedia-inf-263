import cv2
import numpy as np
import matplotlib.pyplot as plt

ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/"
ninio = cv2.imread(ruta + "ninio.jpg")
ninio_nuevo = ruta+"ninio_nuevo.jpg"

gris = cv2.cvtColor(ninio, cv2.COLOR_BGR2GRAY)
suavizado = cv2.GaussianBlur(gris, (5,5), 0)
bordes = cv2.Canny(suavizado, 8, 100)

kernel = np.ones((5,5), np.uint8)#aqui se modifica los bordes
bordes_gruesos = cv2.dilate(bordes, kernel, iterations=1)

resplandor = cv2.GaussianBlur(bordes_gruesos,(25,25), 0)

intensidad = (resplandor/255.0)[:,:,np.newaxis]

color_resplandor = np.array([20,75,160],dtype=np.float32)
capa_luz = intensidad*color_resplandor

resultado_f= ninio.astype(np.float32)+(capa_luz+1.2)
resultado = np.clip(resultado_f, 0,255).astype(np.uint8)
resultado[bordes_gruesos>0] = [255,255,0]

cv2.imwrite(ninio_nuevo, resultado)

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

#morphologyex, cierra espacios y completa los contornos
#gausian blur suaviza el ruido de la imagen en alrededore