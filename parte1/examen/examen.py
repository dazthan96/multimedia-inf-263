import os
from moviepy import ImageClip,AudioClip, concatenate_videoclips
import cv2
import matplotlib.pyplot as plt
import numpy as np
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/examen/recursos/"
ruta_video = ruta + "Frosty.mp4"
ruta_frames = ruta + "frames/"

# video = cv2.VideoCapture(ruta_video)
# contador = 1
# while True:
#     retorno, frame = video.read()
#     if not retorno:
#         break
#     ruta_frame = ruta_frames+f'frame_{contador:04d}.jpg'
#     cv2.imwrite(ruta_frame, frame)
#     contador +=1
# video.release()

imagenes = os.listdir(ruta_frames)
imagenes.sort()
frames_prueba= cv2.imread(ruta_frames+imagenes[-1])
frames_rgb = cv2.cvtColor(frames_prueba, cv2.COLOR_BGR2RGB)

alto, ancho = frames_prueba.shape[:2]
imagen_prueba = imagenes[0]

imagen = cv2.imread(ruta_frames+imagen_prueba)
print(ruta_frames+imagen_prueba)
original = imagen.copy()
y1,y2= 20,286
x1,x2= 172,377
alto = y2-y1
ancho = x2-x1
muneco=cv2.resize(original, (alto, ancho,))
muneco = original[y1:y2, x1:x2]
imagen_color = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
suavizado = cv2.GaussianBlur(original, (5,5), 0)
bordes = cv2.Canny(suavizado, 8, 100)


#codec = cv2.VideoWriter_fourcc(*'mp4v')
#video_salida = cv2.VideoWriter(ruta+"videos/video_reconstruido.mp4", codec, 24, (ancho, alto))
#
# for imagen in imagenes:
#     frame = cv2.imread(ruta_frames + imagen)
#     frame = cv2.resize(frame, (ancho, alto))
    
#     gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     bordes = cv2.Canny(gris, 100, 200)
    
#     bordes_invertidos = cv2.bitwise_not(bordes)
#     resultado = cv2.cvtColor(bordes_invertidos, cv2.COLOR_GRAY2BGR)
    
    
#     video_salida.write(resultado)


# video_salida.release()

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(muneco, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(imagen_gris, cv2.COLOR_BGR2RGB))
plt.title("gris")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(bordes, cv2.COLOR_BGR2RGB))
plt.title("bordes")
plt.axis("off")

plt.tight_layout()
plt.show()