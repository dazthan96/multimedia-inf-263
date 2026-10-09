import asyncio
import edge_tts
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/resource/"
voz_seleccionada = "es-ES-AlvaroNeural"
texto="ejemplo de lectura mediante texto insertado manualmente"
ruta_audio_salida=ruta+"voz_dictada.mp3"
async def generar_audio()->None:
    comunicador = edge_tts.Communicate(text=texto, voice=voz_seleccionada)
    await comunicador.save(ruta_audio_salida)
    print("audio generado exitosamente")
#await genera_audio()
if __name__ == "__main__":
    asyncio.run(generar_audio())
