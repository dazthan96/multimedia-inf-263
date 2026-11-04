import os
import subprocess
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
ruta_audio = ruta+"voz_dictada.mp3"
ruta_video = ruta +"video_reconstruido.mp4"
ruta_video_voz = ruta + "video_con_voz.mp4"

if os.path.exists(ruta_video) and os.path.exists(ruta_audio):
    size_video=os.path.getsize(ruta_video)
    size_audio=os.path.getsize(ruta_audio)
    if size_video==0 or size_audio==0:
        print("Uno de los archivos esta vacio")
    else:
        print("Archivos validados")
        cmd=[
            "ffmpeg","-y",
            "-i",ruta_video,
            "-i",ruta_audio,
            "-map","0:v:0",
            "-map","1:a:0",
            "-c:v","copy",
            "-c:a","aac",
            "-shortest",
            ruta_video_voz
        ]
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        if resultado.returncode==0:
            print(f"Proceso completado y guardado en: {ruta_video_voz}")
        else:
            print(f"error:{resultado.stderr}")
else:
    print("Archivos n encontrados")