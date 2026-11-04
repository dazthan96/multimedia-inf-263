import cv2
import os

#CAPTURAR IMAGENES DE UNA VIDEO#
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
ruta_video = ruta + "video_prueba.mp4"

video = cv2.VideoCapture(ruta_video)

contador = 1

while True:
    retorno, frame = video.read()
    if not retorno:
        break
    ruta_frame = ruta+"frames/"+f'/frame_{contador:03d}.jpg'
    cv2.imwrite(ruta_frame, frame)
    contador +=1
video.release()
print(f"frames extraidos: {contador -1}")