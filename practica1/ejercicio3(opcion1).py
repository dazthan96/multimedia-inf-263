import cv2
import numpy as np

ruta_base="E:/facu/06semestre/multimedia-inf-263/practica1/"
ruta_video = "recursos/video_ejerc3.mp4"
cap = cv2.VideoCapture(ruta_base+ruta_video)

if not cap.isOpened():
    print(f"Error: No se pudo abrir el video desde '{ruta_base+ruta_video}'.")
else:
    ret_temp, frame_temp = cap.read()
    if not ret_temp:
        print("Error: El archivo de video está vacío o corrupto.")
        cap.release()
        exit()

    alto, ancho, canales = frame_temp.shape
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(ruta_base+"resultados/ejercicio3(opcion1).mp4", fourcc, fps, (ancho, alto))

    es_primer_fotograma = True

    while True:
        ret, fotograma = cap.read()

        if not ret:
            break

        mitad_alto = alto // 2

        superior_original = fotograma[0:mitad_alto, :]

        inferior_original = fotograma[mitad_alto:alto, :]

        gris_base = cv2.cvtColor(inferior_original, cv2.COLOR_BGR2GRAY)

        bordes = cv2.Canny(gris_base, 80, 100)

        kernel = np.ones((2, 2), np.uint8)
        bordes_gruesos = cv2.dilate(bordes, kernel, iterations=1)

        gris_con_bordes = gris_base.copy()
        gris_con_bordes[bordes_gruesos == 255] = 0

        inferior_procesada = cv2.cvtColor(gris_con_bordes, cv2.COLOR_GRAY2BGR)

        fotograma_final = np.vstack((superior_original, inferior_procesada))

        if es_primer_fotograma:
            cv2.imwrite(ruta_base+"resultados/ejercicio3(opcion1).png", fotograma_final)
            print("Primer fotograma guardado con éxito como 'ejercicio3.png'")
            es_primer_fotograma = False

        out.write(fotograma_final)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video completo procesado y guardado como 'ejercicio3.mp4'")
