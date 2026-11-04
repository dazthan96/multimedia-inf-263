import cv2
import numpy as np

# 1. Configuración de rutas y carga de la imagen
ruta_base = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/"
img_original = cv2.imread(ruta_base + "ninio.jpg")

# Copias de seguridad para no alterar la matriz original durante el proceso
img_procesar = img_original.copy()
resultado_final = img_original.copy()

# 2. Preprocesamiento y detección de bordes base
gris = cv2.cvtColor(img_procesar, cv2.COLOR_BGR2GRAY)
# Filtro bilateral para eliminar ruido de fondo manteniendo bordes nítidos del objeto
suavizado = cv2.bilateralFilter(gris, 9, 75, 75)
# Canny adaptativo para capturar los límites del objeto principal
bordes_base = cv2.Canny(suavizado, 30, 100)

# 3. Operaciones morfológicas para aislar el contorno y definir la región "Bordes"
# Kernel estructural intermedio para cerrar huecos en la silueta
kernel_cierre = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
bordes_cerrados = cv2.morphologyEx(bordes_base, cv2.MORPH_CLOSE, kernel_cierre)

# Kernel de dilatación para engrosar y estilizar artísticamente la región "Bordes"
kernel_borde_artistico = np.ones((5, 5), np.uint8)
region_bordes = cv2.dilate(bordes_cerrados, kernel_borde_artistico, iterations=1)

# 4. Segmentación automática de las regiones (Máscaras)
contornos, _ = cv2.findContours(bordes_cerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear máscaras binarias del tamaño de la imagen original
mascara_interior = np.zeros(gris.shape, dtype=np.uint8)
mascara_fondo = np.zeros(gris.shape, dtype=np.uint8)

if contornos:
    # Selección automática basada en el área del contorno máximo (sin coordenadas fijas)
    contorno_objeto = max(contornos, key=cv2.contourArea)
    
    # Máscara 1: Interior del objeto completo (relleno de color blanco = 255)
    cv2.drawContours(mascara_interior, [contorno_objeto], -1, 255, -1)
    
    # Máscara 2: Fondo exterior (Inversa matemática exacta de la máscara interior)
    mascara_fondo = cv2.bitwise_not(mascara_interior)

# 5. Definición de la paleta de colores para la reconstrucción estilizada
color_interior = np.array([0, 0, 255])    # Rojo sólido en formato BGR
color_fondo = np.array([255, 0, 0])       # Azul sólido en formato BGR
color_bordes = np.array([0, 255, 255])    # Amarillo sólido en formato BGR

# 6. Construcción y asignación por regiones sobre la imagen de salida
# Región Fondo Exterior: Donde la máscara del fondo está activa (255)
resultado_final[mascara_fondo == 255] = color_fondo

# Región Interior del Objeto: Donde la máscara del interior está activa (255)
resultado_final[mascara_interior == 255] = color_interior

# Región Bordes: Superpuesta al final para delimitar limpiamente el objeto del fondo
resultado_final[region_bordes > 0] = color_bordes

# 7. Generación de la vista comparativa (Tres paneles)
# Convertir el mapa de bordes gris de 1 canal a BGR de 3 canales para poder concatenarlo con las fotos a color
bordes_visualizacion = cv2.cvtColor(region_bordes, cv2.COLOR_GRAY2BGR)

# Concatenación horizontal: Original | Mapa de Bordes | Reconstrucción Final
vista_comparativa = np.hstack((img_original, bordes_visualizacion, resultado_final))

# 8. Almacenamiento de resultados en el disco
cv2.imwrite(ruta_base + "reconstruccion_artistica.jpg", resultado_final)
cv2.imwrite(ruta_base + "vista_comparativa_tres_regiones.jpg", vista_comparativa)
