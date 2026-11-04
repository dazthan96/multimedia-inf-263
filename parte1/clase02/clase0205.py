import matplotlib.pyplot as plt
import os
import cv2
#ORDENAR Y CAPTURA LA ULTIMA IMAGEN DE LOS FRAMES#
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
ruta_frames = ruta+"frames/"
imagenes = os.listdir(ruta_frames)
imagenes.sort()
frames_prueba= cv2.imread(ruta_frames+imagenes[-1])
frames_rgb = cv2.cvtColor(frames_prueba, cv2.COLOR_BGR2RGB)
#PARA CREAR EL VIDEO A PARTIR DE LAS IMAGENES FRAMES#

# plt.figure(figsize=(8,6))
# plt.imshow(frames_rgb)
# plt.axis("off")
# plt.title("Ultima imagen del directorio")
# plt.show()

alto, ancho = frames_prueba.shape[:2] #SHAPE RETORNA UNA LISTA DE VARIOS ATRIBUTOS, LOS DOS PRIMEROS SON ALTO Y ANCHO, POR ESO DEBEMOS RESTRINGIR LOS DOS PRIMEROS VALORES DE LA LISTA#
print(f"Alto: {alto}, Ancho: {ancho}")

codec = cv2.VideoWriter_fourcc(*'mp4v')
video_salida = cv2.VideoWriter(ruta+"video_reconstruido.mp4", codec, 30, (ancho, alto))

for imagen in imagenes:
    frame = cv2.imread(ruta_frames+imagen)
    frame = cv2.resize(frame, (ancho, alto))
    
    video_salida.write(frame)

video_salida.release()
print("video guardado")