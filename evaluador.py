from modelo import generar_respuesta

def evaluar_mensaje(mensaje):
    prompt = f"""
You are an assistant that detects only if a message indicates a risk of self-harm, suicide, or harming others.
Classify the following message as either "risk" or "normal". 
- "risk" means the message explicitly mentions suicide, killing, or self-harm intentions.
- "normal" means it does not.

Message: "{mensaje}"

Classification:"""

    respuesta = generar_respuesta(prompt)
    # Extraer texto después de "Classification:"
    if "Classification:" in respuesta:
        clasificacion = respuesta.split("Classification:")[1].strip().lower()
        # Solo tomar la primera palabra para evitar respuestas largas
        clasificacion = clasificacion.split()[0]  
        if clasificacion == "risk":
            return "risk"
        else:
            return "normal"
    else:
        # Si no se encuentra "Classification:", asumir normal
        return "normal"
