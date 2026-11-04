import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import cv2
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/simulacro_examen/recursos/"
ruta_audio = [ruta + "audio/dialogo1.mp3", ruta + "audio/dialogo2.mp3", ruta + "audio/dialogo3.mp3", ruta + "audio/dialogo4.mp3"]
ruta_imagen = [ruta + "images/imagen1.jpg", ruta + "images/imagen2.jpg", ruta + "images/imagen3.jpg", ruta + "images/imagen4.jpg"]
ruta_video_voz = ruta + "videos/minidocumental.mp4"

# Lista para almacenar los fragmentos de video generados en cada iteración
clips_de_video = []

for i in range(len(ruta_audio)):
    # 1. Validar que existan los elementos en el índice actual [i]
    if os.path.exists(ruta_imagen[i]) and os.path.exists(ruta_audio[i]):
        
        # Corregido: pasar el archivo individual [i] y no la lista completa
        size_audio = os.path.getsize(ruta_audio[i])
        size_imagen = os.path.getsize(ruta_imagen[i])
        imagen=cv2.imread(ruta_imagen[i])
        imagen_rd = cv2.resize(imagen,(500,300))
        if size_audio == 0 or size_imagen == 0:
            print(f"Error: El archivo de audio o imagen en el índice {i} está vacío.")
            continue
            
        print(f"Validando par {i+1}: Imagen y Audio detectados correctamente.")
        
        try:
            # 2. Cargar el audio para conocer su duración exacta
            audio_clip = AudioFileClip(ruta_audio[i])
            duracion = audio_clip.duration
            
            # 3. Crear el clip de video a partir de la imagen estática con la duración del audio
            # Nota: Usamos las dimensiones (500, 300) que definiste originalmente
            video_clip = (ImageClip(imagen_rd).with_duration(duracion))
            
            # 4. Fusionar el audio con el clip de la imagen
            video_con_audio = video_clip.with_audio(audio_clip)
            
            # 5. Guardar el fragmento en nuestra lista
            clips_de_video.append(video_con_audio)
            
        except Exception as e:
            print(f"Error procesando el par {i+1}: {e}")
    else:
        print(f"Error: No se encontraron los archivos para el índice {i}")

# 6. Concatenar todos los clips guardados en un único video final
if clips_de_video:
    print("\nConcatenando todos los fragmentos en el video final...")
    try:
        # Junta todos los miniclips uno detrás de otro
        video_final = concatenate_videoclips(clips_de_video, method="compose")
        
        # Exportar el resultado final al archivo único
        video_final.write_videofile(
            ruta_video_voz, 
            fps=24,             # Especificar FPS es obligatorio para clips de imágenes
            codec="libx264", 
            audio_codec="aac",
            logger="bar"        # Muestra una barra de progreso en la consola
        )
        
        # Cerrar los clips para liberar la memoria del sistema
        video_final.close()
        for clip in clips_de_video:
            clip.close()
            
        print(f"\n¡Proceso completado exitosamente! Video guardado en: {ruta_video_voz}")
        
    except Exception as e:
        print(f"Error al exportar el video final: {e}")
else:
    print("No se generó ningún clip válido para concatenar.")

