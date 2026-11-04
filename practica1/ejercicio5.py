import cv2
import numpy as np

ruta_base="E:/facu/06semestre/multimedia-inf-263/practica1/"
ruta_video = "recursos/video_ejer5.mp4"
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
    out = cv2.VideoWriter(ruta_base+"resultados/ejercicio5.mp4", fourcc, fps, (ancho, alto))

    es_primer_fotograma = True

    while True:
        ret, fotograma = cap.read()

        if not ret:
            break

        imagen_suave = cv2.GaussianBlur(fotograma, (3, 3), 0)

        gris = cv2.cvtColor(imagen_suave, cv2.COLOR_BGR2GRAY)

        bordes = cv2.Canny(gris, 20, 40)

        #cone sta linea de codigo, al ya no utilizar bordes anchos con dilate, los debemos pasarle los bordes, sera mas fino
        boceto_gris = cv2.bitwise_not(bordes)
        
        #Al comentar esto, los bordes seran mas finos y con mas detalles
        #kernel_trazo = np.ones((2, 2), np.uint8)
        # bordes_dilatados = cv2.dilate(bordes, kernel_trazo, iterations=1)
        # boceto_gris = cv2.bitwise_not(bordes_dilatados)

        fotograma_final = cv2.cvtColor(boceto_gris, cv2.COLOR_GRAY2BGR)

        if es_primer_fotograma:
            cv2.imwrite(ruta_base+"resultados/ejercicio5.png", fotograma_final)
            print("Muestra del primer fotograma guardada como 'ejercicio5.png'")
            es_primer_fotograma = False

        out.write(fotograma_final)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video guardado como 'ejercicio5.mp4'")
