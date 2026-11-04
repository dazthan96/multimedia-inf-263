import asyncio
import edge_tts

# Configuración de rutas y parámetros
ruta = "C:/Users/Beto/Documents/avance 2026-II/multimedia/simulacro_examen/recursos/audio/"
#ruta_audio = ruta + "voz_cantando_simple.mp3"
voz = "es-MX-DaliaNeural"
lista_texto=[
    "El pangolín es el único mamífero del mundo completamente cubierto de escamas de queratina",
    "...Son animales insectívoros especializados en consumir hormigas y termitas.",
    "...Cuando detecta una amenaza, el pangolín se enrolla por completo formando una bola rígida e impenetrable, escondiendo su cabeza y zonas blandas bajo la dura capa de escamas.",
    "...Tienen hábitos principalmente nocturnos y solitarios"]


async def generar_audio():
    contador = 1
    for texto in lista_texto:
        comunicador = edge_tts.Communicate(
            text=texto, 
            voice=voz, 
            rate="-20%", 
            pitch="+50Hz"
        )
        await comunicador.save(ruta+f"dialogo{contador}.mp3")
        contador = contador + 1
    print("audio generado correctamente")

# Ejecutar la función asíncrona en el entorno de Jupyter
#generar_audio()
if __name__ == "__main__":
    asyncio.run(generar_audio())