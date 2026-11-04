import cv2
import numpy as np

ruta_base="E:/facu/06semestre/multimedia-inf-263/practica1/"
ruta_video = "recursos/video_ejer4.mp4"
cap = cv2.VideoCapture(ruta_base+ruta_video)

if not cap.isOpened():
    print(f"Error: No se pudo abrir el video desde '{ruta_base+ruta_video}'.")
else:
    ret_temp, frame_temp = cap.read()
    if not ret_temp:
        cap.release()
        exit()

    alto, ancho, canales = frame_temp.shape

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    total_fotogramas = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    tamano_segmento = total_fotogramas // 5

    limite_rojo = tamano_segmento
    limite_verde = tamano_segmento * 2
    limite_azul = tamano_segmento * 3
    limite_negativo = tamano_segmento * 4

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(ruta_base+"resultados/ejercicio4.mp4", fourcc, fps, (ancho, alto))

    contador_frames = 0
    es_primer_fotograma = True

    while True:
        ret, fotograma = cap.read()

        if not ret:
            break

        fotograma_procesado = fotograma.copy()

        if contador_frames < limite_rojo:
            fotograma_procesado[:, :, 0] = 0
            fotograma_procesado[:, :, 1] = 0

        elif contador_frames < limite_verde:
            fotograma_procesado[:, :, 0] = 0
            fotograma_procesado[:, :, 2] = 0

        elif contador_frames < limite_azul:
            fotograma_procesado[:, :, 1] = 0
            fotograma_procesado[:, :, 2] = 0

        elif contador_frames < limite_negativo:
            fotograma_procesado = 255 - fotograma

        else:
            fotograma_procesado = fotograma

        if es_primer_fotograma:
            cv2.imwrite(ruta_base+"resultados/ejercicio4.png", fotograma_procesado)
            print("Muestra del primer fotograma guardada como 'ejercicio4.png'")
            es_primer_fotograma = False

        out.write(fotograma_procesado)
        contador_frames += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video completo guardado exitosamente como 'ejercicio4.mp4'")
