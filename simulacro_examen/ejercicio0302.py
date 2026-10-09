import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import cv2
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/simulacro_examen/recursos/"
ruta_audio = [ruta + "audio/dialogo1.mp3", ruta + "audio/dialogo2.mp3", ruta + "audio/dialogo3.mp3", ruta + "audio/dialogo4.mp3"]
ruta_imagen = [ruta + "images/imagen1.jpg", ruta + "images/imagen2.jpg", ruta + "images/imagen3.jpg", ruta + "images/imagen4.jpg"]
ruta_video_voz = ruta + "videos/minidocumental.mp4"

clips_de_video = []

for i in range(len(ruta_audio)):
    if os.path.exists(ruta_imagen[i]) and os.path.exists(ruta_audio[i]):
        size_audio = os.path.getsize(ruta_audio[i])
        size_imagen = os.path.getsize(ruta_imagen[i])
        imagen=cv2.imread(ruta_imagen[i])
        imagen_rd = cv2.resize(imagen,(500,300))
        if size_audio == 0 or size_imagen == 0:
            print(f"Error: El archivo de audio o imagen en el índice {i} está vacío.")
            continue
            
        print(f"Validando par {i+1}: Imagen y Audio detectados correctamente.")
        
        try:
            audio_clip = AudioFileClip(ruta_audio[i])
            duracion = audio_clip.duration
            
            video_clip = (ImageClip(imagen_rd).with_duration(duracion))
            
            video_con_audio = video_clip.with_audio(audio_clip)
            
            clips_de_video.append(video_con_audio)
            
        except Exception as e:
            print(f"Error procesando el par {i+1}: {e}")
    else:
        print(f"Error: No se encontraron los archivos para el índice {i}")

if clips_de_video:
    print("\nConcatenando todos los fragmentos en el video final...")
    try:
        video_final = concatenate_videoclips(clips_de_video, method="compose")
        
        video_final.write_videofile(
            ruta_video_voz, 
            fps=24,    
            codec="libx264", 
            audio_codec="aac",
            logger="bar"        
        )
        
        video_final.close()
        for clip in clips_de_video:
            clip.close()
            
        print(f"\n¡Proceso completado exitosamente! Video guardado en: {ruta_video_voz}")
        
    except Exception as e:
        print(f"Error al exportar el video final: {e}")
else:
    print("No se generó ningún clip válido para concatenar.")

