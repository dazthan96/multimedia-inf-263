import cv2
import matplotlib.pyplot as plt
import numpy as np
ruta_base="E:/facu/06semestre/multimedia-inf-263/practica1/"
ruta_imagen = "recursos/imagen_ejer1.jpeg"
ruta_imagen_result="resultados/ejercicio1.png"
imagen_bgr = cv2.imread(ruta_base+ruta_imagen)

if imagen_bgr is None:
    print(
        f"Error: No se pudo cargar la imagen desde '{ruta_base+ruta_imagen}'. Verifica la ruta."
    )
else:
    imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)
    imagen_suave = cv2.GaussianBlur(imagen_rgb, (5, 5), 0)
    imagen_gris = cv2.cvtColor(imagen_suave, cv2.COLOR_RGB2GRAY)
    bordes = cv2.Canny(imagen_gris, 50, 150)

    kernel_dilatacion = np.ones((2, 5), np.uint8)
    bordes_dilatados = cv2.dilate(bordes, kernel_dilatacion, iterations=1)

    bordes_invertidos = cv2.bitwise_not(bordes_dilatados)

    bordes_rgb = cv2.cvtColor(bordes_invertidos, cv2.COLOR_GRAY2RGB)

    resultado_final_rgb = cv2.bitwise_and(imagen_suave, bordes_rgb)

    resultado_final_bgr = cv2.cvtColor(resultado_final_rgb, cv2.COLOR_RGB2BGR)
    imagen_final = np.hstack((imagen_bgr, resultado_final_bgr))
    cv2.imwrite(ruta_base+ruta_imagen_result, imagen_final)
    print("Imagen guardada como 'ejercicio1.png'")

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(imagen_rgb)
    plt.title("Imagen Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(resultado_final_rgb)
    plt.title("Resultado (Efecto Dibujo)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
