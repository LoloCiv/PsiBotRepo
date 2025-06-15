from transformers import pipeline

# CARGAMOS PIPELINE DE CLASIFICACIÓN
clasificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# PALABRAS CLAVE AMPLIADAS PARA DETECCIÓN DE RIESGO
PALABRAS_CLAVE = [
    "kill", "i want to kill", "kill myself", "suicide", "cut", "cut myself",
    "end my life", "no reason to live", "want to die", "hurt myself", "hate myself"
]

def evaluar_mensaje(mensaje):
    lower_msg = mensaje.lower()

    # FILTRO RÁPIDO POR PALABRAS CLAVE
    if any(palabra in lower_msg for palabra in PALABRAS_CLAVE):
        return "risk"

    # CLASIFICADOR DE EMOCIONES COMO RESPALDO
    resultado = clasificador(mensaje)[0]
    label = resultado["label"]
    score = resultado["score"]

    if label == "NEGATIVE" and score > 0.95:
        return "risk"

    return "safe"
