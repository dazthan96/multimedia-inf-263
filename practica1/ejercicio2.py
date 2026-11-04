import cv2
import matplotlib.pyplot as plt
import numpy as np

ruta_base="E:/facu/06semestre/multimedia-inf-263/practica1/"
ruta_img1 = "recursos/imagen_ejer2.jpeg"
ruta_img2 = "recursos/fondo_ejer2.jpg"

img1_bgr = cv2.imread(ruta_base+ruta_img1)
img2_bgr = cv2.imread(ruta_base+ruta_img2)

if img1_bgr is None or img2_bgr is None:
    print("Error: Asegúrate de que ambas imágenes existen en la ruta indicada.")
else:
    img1 = cv2.cvtColor(img1_bgr, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2_bgr, cv2.COLOR_BGR2RGB)

    ymin, ymax = 117, 325
    xmin, xmax = 314, 519
    recorte = img1[ymin:ymax, xmin:xmax]

    alto_final, ancho_final, canales = img2.shape
    ancho_tercio = ancho_final // 3
    nuevo_ancho = int(ancho_tercio * 0.6)
    nuevo_alto = nuevo_ancho
    
    recorte_escalado = cv2.resize(recorte, (nuevo_ancho, nuevo_alto), interpolation=cv2.INTER_LINEAR)

    fondo_suave = cv2.GaussianBlur(img2, (11, 11), 0)

    margen_x = (ancho_tercio - nuevo_ancho) // 2
    pos_x_izq = margen_x
    pos_x_cen = ancho_tercio + margen_x
    pos_x_der = (2 * ancho_tercio) + margen_x
    
    pos_y = (alto_final - nuevo_alto) // 2


    comp_original = fondo_suave.copy()
    comp_original[pos_y:pos_y+nuevo_alto, pos_x_izq:pos_x_izq+nuevo_ancho] = recorte_escalado
    comp_original[pos_y:pos_y+nuevo_alto, pos_x_cen:pos_x_cen+nuevo_ancho] = recorte_escalado
    comp_original[pos_y:pos_y+nuevo_alto, pos_x_der:pos_x_der+nuevo_ancho] = recorte_escalado

    comp_transparencia = fondo_suave.copy()

    posiciones_x = [pos_x_izq, pos_x_cen, pos_x_der]
    for i, px in enumerate(posiciones_x):
        if i == 1:
            roi_fondo = comp_transparencia[
                pos_y : pos_y + nuevo_alto, px : px + nuevo_ancho
            ]
            objeto_final = cv2.addWeighted(
                recorte_escalado, 0.3, roi_fondo, 1.0-0.3, 0
            )
        else:
            objeto_final = recorte_escalado

        comp_transparencia[
            pos_y : pos_y + nuevo_alto, px : px + nuevo_ancho
        ] = objeto_final
    
    comp_gris_1can = cv2.cvtColor(comp_original, cv2.COLOR_RGB2GRAY)
    comp_gris = cv2.cvtColor(comp_gris_1can, cv2.COLOR_GRAY2RGB)

    comp_negativo = 255 - comp_original

    resultado_triptico = np.zeros((alto_final, ancho_final, canales), dtype=np.uint8)

    resultado_triptico[:, 0:ancho_tercio] = comp_transparencia[:, 0:ancho_tercio]
    resultado_triptico[:, ancho_tercio:2*ancho_tercio] = comp_gris[:, ancho_tercio:2*ancho_tercio]
    resultado_triptico[:, 2*ancho_tercio:ancho_final] = comp_negativo[:, 2*ancho_tercio:ancho_final]

    resultado_final_bgr = cv2.cvtColor(resultado_triptico, cv2.COLOR_RGB2BGR)
    cv2.imwrite(ruta_base+"resultados/ejercicio2.png", resultado_final_bgr)
    print("Imagen guardada como 'ejercicio2.png'")

    plt.figure(figsize=(15, 5))

    plt.imshow(resultado_triptico)
    plt.title("Resultado Final: Original | Grises | Negativo")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
