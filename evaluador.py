import re

# Lista básica de palabras clave asociadas a riesgo
PALABRAS_CLAVE_RIESGO = [
    "suicide", "kill myself", "end it all", "die", "disappear", "worthless",
    "hopeless", "no reason to live", "give up", "cut myself", "hurt myself",
    "jump off", "overdose", "hang", "take my life","suicidal thoughts"
]

def clean_response(text):
    text = text.replace("</s>", "").strip()
    text = re.sub(r"\*[^*]+\*", "", text).strip()
    return text.lower()

def evaluar_mensaje(mensaje):
    mensaje_clean = mensaje.lower()
    for palabra in PALABRAS_CLAVE_RIESGO:
        if palabra in mensaje_clean:
            print(f"🔴 Palabra clave detectada: '{palabra}'")
            return "risk"
    return "safe"
