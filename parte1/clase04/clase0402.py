import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de rutas y lectura de la imagen
# Define la carpeta de origen donde se encuentran los recursos visuales
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/images/"
# Lee la imagen original 'ninio.jpg' desde la ruta especificada
ninio = cv2.imread(ruta + "ninio.jpg")
# Define la ruta y el nombre del nuevo archivo donde se guardará el resultado final
ninio_nuevo = ruta+"ninio_nuevo.jpg"

# 2. Detección de bordes
# Convierte la imagen a escala de grises para simplificar el análisis de estructuras y formas
gris = cv2.cvtColor(ninio, cv2.COLOR_BGR2GRAY)
# Aplica un filtro Gaussiano para suavizar la imagen (elimina ruido sutil y detalles innecesarios)
suavizado = cv2.GaussianBlur(gris, (5,5), 0)
# Aplica el algoritmo de Canny en la imagen suavizada usando umbrales bajos (8 y 100) para capturar bastantes bordes
bordes = cv2.Canny(suavizado, 8, 100)

# 3. Engrosamiento de bordes (Morfología)
# Crea una matriz (matriz cuadrada de 5x5 llena de unos) que servirá como molde para la dilatación
kernel = np.ones((5,5), np.uint8) # Aquí se modifica el grosor estructural de los bordes
# Expande (dilata) los bordes blancos de la imagen usando el kernel, haciéndolos más gruesos en 1 iteración
bordes_gruesos = cv2.dilate(bordes, kernel, iterations=1)

# 4. Creación del efecto de resplandor (Glow)
# Aplica un desenfoque Gaussiano muy alto (núcleo de 25x25) a los bordes gruesos para simular una luz difuminada
resplandor = cv2.GaussianBlur(bordes_gruesos,(25,25), 0)

# 5. Normalización y ajuste de dimensiones
# Divide entre 255.0 para pasar los valores de 0-255 a un rango flotante de 0.0 a 1.0, 
# e introduce un eje extra (np.newaxis) para que la matriz sea 3D y coincida con los canales BGR
intensidad = (resplandor/255.0)[:,:,np.newaxis]

# 6. Aplicación de color al resplandor
# Define el color base para el brillo en formato BGR flotante [Azul=20, Verde=75, Rojo=160] (un tono naranja/marrón)
color_resplandor = np.array([20,75,160],dtype=np.float32)
# Multiplica la intensidad del mapa difuminado por el color elegido para crear la capa de luz coloreada
capa_luz = intensidad*color_resplandor

# 7. Combinación con la imagen original y toque final
# Suma la imagen original convertida a flotante con la capa de luz más un extra constante (+1.2) para iluminar el fondo
resultado_f= ninio.astype(np.float32)+(capa_luz+1.2)
# Limita los valores resultantes para que no superen 255 ni bajen de 0, y los reconvierte al tipo entero estándar de 8 bits
resultado = np.clip(resultado_f, 0,255).astype(np.uint8)
# Sobre la imagen final, busca los píxeles de los bordes gruesos y los pinta de color [Azul=255, Verde=255, Rojo=0] (Cian/Celeste)
resultado[bordes_gruesos>0] = [255,255,0]

# 8. Guardado del resultado
# Guarda la imagen resultante procesada en el disco con el nombre configurado al inicio
cv2.imwrite(ninio_nuevo, resultado)


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(ninio, cv2.COLOR_BGR2RGB))
plt.title("imagen original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("imagen bordes remarcados")
plt.axis("off")

plt.tight_layout()
plt.show()

#morphologyex, cierra espacios y completa los contornos
#gausian blur suaviza el ruido de la imagen en alrededore