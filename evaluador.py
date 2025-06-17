import re

PALABRAS_CLAVE_RIESGO = [
    "suicide", "kill myself", "killing myself", "want to kill myself",
    "end it all", "end my life", "end everything",
    "die", "dying", "want to die", "i want to die",
    "disappear", "vanish", "go away forever",
    "worthless", "useless", "nothing matters",
    "hopeless", "helpless", "no hope",
    "no reason to live", "no purpose", "don't want to live",
    "give up", "i gave up", "i'm giving up",
    "cut myself", "cutting", "cutting myself",
    "hurt myself", "hurting myself", "self harm",
    "jump off", "jumping", "jump from",
    "overdose", "take too many pills", "pill overdose",
    "hang", "hanging", "hang myself",
    "take my life", "taking my life",
    "suicidal thoughts", "suicidal", "thinking of suicide"
]
def clean_response(text):
    text = text.replace("</s>", "").strip()
    text = re.sub(r"\*[^*]+\*", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower().strip()

def evaluar_mensaje(mensaje):
    mensaje_clean = clean_response(mensaje.lower())
    for palabra in PALABRAS_CLAVE_RIESGO:
        if palabra in mensaje_clean:
            print(f"🔴 Palabra clave detectada: '{palabra}'")
            return "risk"
    print("🟢 No se detectaron palabras de riesgo.")
    return "safe"
