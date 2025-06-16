import re
from modelo import generar_respuesta_evaluador

def clean_response(text):
    text = text.replace("</s>", "").strip()
    text = re.sub(r"\*[^*]+\*", "", text).strip()
    return text.lower()

def evaluar_mensaje(mensaje):
    prompt = (
        "You are a sensitive assistant that detects if a message contains suicidal thoughts, self-harm risk, or dangerous behavior.\n"
        "Respond only with 'risk' or 'safe'.\n\n"
        f"Message: \"{mensaje}\"\n\n"
        "Response:"
    )

    respuesta = generar_respuesta_evaluador(prompt)
    print(f"\n--- DEBUG RESPUESTA COMPLETA ---\n{respuesta}\n------------------------", flush=True)

    # Extraer primera palabra (formato seguro)
    respuesta_generada = clean_response(respuesta).split()[0]

    print(f"Evaluación extraída: {respuesta_generada}")

    if "risk" in respuesta_generada:
        return "risk"

    return "safe"
