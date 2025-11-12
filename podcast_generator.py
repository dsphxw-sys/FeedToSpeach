from gtts import gTTS
import os

def generar_guion(noticias):
    guion = "Bienvenidos a tu resumen diario de noticias. Empezamos:\n\n"
    for noticia in noticias:
        guion += f"{noticia['titulo']}. {noticia['resumen']}\n\n"
    return guion

def texto_a_audio(texto, archivo_salida):
    tts = gTTS(text=texto, lang='es')
    os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)
    tts.save(archivo_salida)