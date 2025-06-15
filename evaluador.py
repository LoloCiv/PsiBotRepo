
from modelo import generar_respuesta_evaluador

def evaluar_mensaje(mensaje):
    prompt = (
        "You are a sensitive assistant that detects if a message contains suicidal thoughts, self-harm risk, or dangerous behavior.\n"
        "Respond only with 'risk' or 'safe'.\n\n"
        f"Message: \"{mensaje}\"\n\n"
        "Response:"
    )
    respuesta = generar_respuesta_evaluador(prompt)
    respuesta_final = respuesta[len(prompt):].strip().lower()

    if respuesta_final.startswith("risk"):
        return "risk"
    return "safe"
