def evaluar_mensaje(mensaje):
    prompt = f"""
    You are an assistant that detects only if a message indicates a risk of self-harm, suicide, or harming others.
    Classify the following message as either "risk" or "normal". 
    - "risk" means the message explicitly mentions suicide, killing, or self-harm intentions.
    - "normal" means it does not.

    Message: "{mensaje}"

    Classification:"""

    respuesta = generar_respuesta(prompt)
    # Parsear respuesta para obtener la clasificación
    if "risk" in respuesta.lower():
        return "risk"
    else:
        return "normal"
