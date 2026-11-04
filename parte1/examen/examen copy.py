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

imagen = cv2.imread(ruta_frames + imagen_prueba)
y1, y2 = 20, 286
x1, x2 = 172, 377

muneco = imagen[y1:y2, x1:x2].copy()
alto, ancho = muneco.shape[:2]

suavizado = cv2.GaussianBlur(muneco, (5, 5), 0)
bordes = cv2.Canny(suavizado, 8, 100)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
bordes_cerrados = cv2.dilate(bordes, kernel, iterations=1)

contornos, _ = cv2.findContours(bordes_cerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

mascara_interior = np.zeros((alto, ancho), dtype=np.uint8)

if contornos:
    cv2.drawContours(mascara_interior, contornos, -1, (255), thickness=cv2.FILLED)

mascara_exterior = cv2.bitwise_not(mascara_interior)

capa_azul = np.zeros_like(muneco)
capa_azul[:] = (255, 0, 0)
mezcla_azul = cv2.addWeighted(muneco, 0.6, capa_azul, 0.4, 0)


capa_amarilla = np.zeros_like(muneco)
capa_amarilla[:] = (0, 255, 255)
mezcla_amarilla = cv2.addWeighted(muneco, 0.6, capa_amarilla, 0.4, 0)
mascara_2 = mascara_exterior[:, :, np.newaxis]

muneco_fondo_azul = np.where(mascara_2[-1] == 255, mezcla_azul, muneco)

muneco_fondo_amarillo = np.where(mascara_2[-1] == 255, mezcla_amarilla, muneco)

resultado_final = np.hstack((muneco, muneco_fondo_azul, muneco_fondo_amarillo))


cv2.imwrite(ruta+'resultado_muneco_fondos.jpg', resultado_final)

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
plt.imshow(cv2.cvtColor(muneco_fondo_azul, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(muneco_fondo_amarillo, cv2.COLOR_BGR2RGB))
plt.title("gris")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(resultado_final, cv2.COLOR_BGR2RGB))
plt.title("bordes")
plt.axis("off")

plt.tight_layout()
plt.show()