import os
from moviepy import VideoFileClip, AudioFileClip

ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
ruta_audio = ruta + "voz_cantando_simple.mp3"
ruta_video = ruta + "video_bandera.mp4"
ruta_video_voz = ruta + "video_con_voz.mp4"

if os.path.exists(ruta_video) and os.path.exists(ruta_audio):
    size_video = os.path.getsize(ruta_video)
    size_audio = os.path.getsize(ruta_audio)
    
    if size_video == 0 or size_audio == 0:
        print("Uno de los archivos está vacío")
    else:
        print("Archivos validados. Iniciando fusión con MoviePy...")
        try:
            video_clip = VideoFileClip(ruta_video)
            audio_clip = AudioFileClip(ruta_audio)
            
            duracion_final = min(video_clip.duration, audio_clip.duration)
            
            video_recortado = video_clip.with_duration(duracion_final)
            audio_recortado = audio_clip.with_duration(duracion_final)
            
            video_final = video_recortado.with_audio(audio_recortado)
            
            video_final.write_videofile(
                ruta_video_voz, 
                codec="libx264", 
                audio_codec="aac",
                logger=None)
            
            video_clip.close()
            audio_clip.close()
            video_final.close()
            
            print(f"Proceso completado y guardado en: {ruta_video_voz}")
            
        except Exception as e:
            print(f"Error durante el procesamiento: {e}")
else:
    print("Archivos no encontrados")
