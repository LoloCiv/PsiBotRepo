from modelo import generar_respuesta_clasificacion


def evaluar_mensaje(mensaje):
    prompt = f"""
You are an assistant that detects only if a message indicates a risk of self-harm, suicide, or harming others.
Classify the following message as either "risk" or "safe" ONLY.

Message: "{mensaje}"

Answer:"""

    respuesta = generar_respuesta_clasificacion(prompt).lower().strip()
    
    if "risk" in respuesta:
        return "risk"
    else:
        return "safe"
