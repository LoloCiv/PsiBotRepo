from transformers import pipeline

# USAMOS MODELO ENTRENADO PARA DETECCIÓN DE RIESGO SUICIDA
clasificador = pipeline("text-classification", model="uw-hai/suicide-risk")

# PALABRAS CLAVE PARA FILTRADO ADICIONAL (BACKUP)
PALABRAS_CLAVE = [
    "kill myself", "i want to kill", "cut", "cut myself", "suicide", "end my life",
    "i want to die", "hurt myself", "hate myself", "no reason to live", "worthless",
    "disappear", "give up"
]

def evaluar_mensaje(mensaje):
    lower_msg = mensaje.lower()

    # FILTRO RÁPIDO POR PALABRAS CLAVE
    if any(palabra in lower_msg for palabra in PALABRAS_CLAVE):
        return "risk"

    # EVALUACIÓN CON MODELO ESPECIALIZADO
    resultado = clasificador(mensaje)[0]
    label = resultado["label"].lower()
    score = resultado["score"]

    if label in ["suicide", "risk"] and score > 0.85:
        return "risk"

    return "safe"
