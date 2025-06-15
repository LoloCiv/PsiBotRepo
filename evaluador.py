from modelo import generar_respuesta_evaluador

def evaluar_mensaje(mensaje):
    prompt = (
        "You are a sensitive assistant that detects if a message contains suicidal thoughts, self-harm risk, or dangerous behavior.\n"
        "Respond only with 'risk' or 'safe'.\n\n"
        f"Message: \"{mensaje}\"\n\n"
        "Response:"
    )

    respuesta = generar_respuesta_evaluador(prompt)
    print(f"\n--- DEBUG RESPUESTA COMPLETA ---\n{respuesta}\n------------------------",flush=True)

    # Intenta extraer solo la respuesta generada
    respuesta_generada = respuesta.replace(prompt, "").strip().lower()
    respuesta_generada = respuesta_generada.split()[0]  # solo la primera palabra

    print(f"Evaluación extraída: {respuesta_generada}")

    if "risk" in respuesta_generada:
        return "risk"
    return "safe"
