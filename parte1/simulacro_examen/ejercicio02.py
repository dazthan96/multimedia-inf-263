import cv2
import os
#CAPTURAR IMAGENES DE UNA VIDEO#
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/simulacro_examen/recursos/"
ruta_video = ruta + "videos/video1.mp4"
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

#ORDENAR Y CAPTURA LA ULTIMA IMAGEN DE LOS FRAMES#
ruta_frames = ruta+"frames/"
imagenes = os.listdir(ruta_frames)
imagenes.sort()
frames_prueba= cv2.imread(ruta_frames+imagenes[-1])
frames_rgb = cv2.cvtColor(frames_prueba, cv2.COLOR_BGR2RGB)

alto, ancho = frames_prueba.shape[:2]

codec = cv2.VideoWriter_fourcc(*'mp4v')
video_salida = cv2.VideoWriter(ruta+"videos/video_reconstruido.mp4", codec, 24, (ancho, alto))

for imagen in imagenes:
    frame = cv2.imread(ruta_frames + imagen)
    frame = cv2.resize(frame, (ancho, alto))
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 100, 200)
    
    bordes_invertidos = cv2.bitwise_not(bordes)
    resultado = cv2.cvtColor(bordes_invertidos, cv2.COLOR_GRAY2BGR)
    
    
    video_salida.write(resultado)


video_salida.release()
print(f"Alto: {alto}, Ancho: {ancho}")
print(f"video guardado en: {ruta}videos/ ")
print(f"Numero de frames: {contador-1}")