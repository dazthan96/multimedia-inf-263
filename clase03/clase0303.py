import asyncio
import edge_tts

# Configuración de rutas y parámetros
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
ruta_audio = ruta + "voz_cantando_simple.mp3"
voz = "es-MX-DaliaNeural"

texto = """ 
Booolivianos el haaado propiiicio... 
Coronooó nuestros votos y anheeelo... 
Es ya liiibre, ya libre este suuuelo... 
ya cesó.. su servil...condición 
"""


async def generar_audio():
    comunicador = edge_tts.Communicate(
        text=texto, 
        voice=voz, 
        rate="-50%", 
        pitch="+50Hz"
    )
    await comunicador.save(ruta_audio)
    print("audio generado correctamente")

# Ejecutar la función asíncrona en el entorno de Jupyter
#generar_audio()
if __name__ == "__main__":
    asyncio.run(generar_audio())
# Mostrar el reproductor de audio en la libreta
#display(Audio(ruta_audio))
