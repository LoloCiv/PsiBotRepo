def evaluar_mensaje(mensaje_usuario):
    prompt = f"""
You are an assistant trained to detect if a person's message represents a risk to their own life or others'.
Your task is to analyze the following message and respond with only one word: RISK or NORMAL.

Message: "{mensaje_usuario}"

Response:"""

    respuesta_cruda = generar_respuesta(prompt)
    respuesta = respuesta_cruda.strip().upper()

    if "RISK" in respuesta:
        return "risk"
    else:
        return "normal"
