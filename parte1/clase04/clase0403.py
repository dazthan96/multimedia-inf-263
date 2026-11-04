import cv2
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np

# 1. Carga de imagen y preprocesamiento de color
# Lee la imagen original del niño desde la ruta del disco
img = cv2.imread("C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/ninio.jpg")
# Convierte la imagen a escala de grises para facilitar la detección de bordes
gris = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

# 2. Suavizado avanzado y detección de bordes
# Aplica un filtro bilateral que reduce el ruido (suaviza texturas) pero conserva los bordes nítidos
suavizado = cv2.bilateralFilter(gris, 9, 75, 75)
# Detecta los bordes en la imagen suavizada usando el algoritmo de Canny con umbrales de 30 y 100
bordes = cv2.Canny(suavizado, 30, 100)

# 3. Operaciones morfológicas para rellenar huecos
# Crea un elemento estructurante (un bloque rectangular de 7x7 píxeles) para procesamiento morfológico
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
# Aplica un cierre morfológico (dilatación seguida de erosión) para unir bordes discontinuos o cerrar siluetas abiertas
bordes_cerrados = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, kernel)

# 4. Búsqueda de contornos y creación de la máscara
# Encuentra los contornos externos en la imagen de bordes cerrados, ignorando las jerarquías internas
contornos, _ = cv2.findContours(bordes_cerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Crea un lienzo completamente negro del mismo tamaño que la imagen en grises para usarlo como máscara
mascara = np.zeros(gris.shape, dtype=np.uint8)

# 5. Selección y rellenado de la silueta principal
# Verifica si se detectó al menos un contorno en el paso anterior
if contornos:
    # Identifica el contorno más grande de la lista basándose en su área calculada
    contorno_mayor = max(contornos, key=cv2.contourArea)
    # Dibuja y rellena (-1) de color blanco (255) el contorno más grande dentro de la máscara negra
    cv2.drawContours(mascara, [contorno_mayor], -1, 255, -1)

# 6. Preparación del nuevo fondo y combinación final
# Crea una imagen completamente negra con las mismas dimensiones y canales de color que la original
fondo = np.zeros_like(img)
# Pinta toda esta nueva imagen de color azul puro en formato BGR [Azul=255, Verde=0, Rojo=0]
fondo[:] = [255, 0, 0]

# Crea una copia exacta de la imagen original para generar el resultado sin dañar los datos fuente
resultado = img.copy()
# Reemplaza los píxeles de la copia por el fondo azul únicamente donde la máscara sea negra (mascara == 0)
resultado[mascara == 0] = fondo[mascara == 0]


plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("bordes")
plt.axis("off")

plt.tight_layout()
plt.show()
