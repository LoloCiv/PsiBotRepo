from modelo import generar_respuesta

conversation_history = []

def clean_response(text):
    text = text.replace("</s>", "").strip()
    text = re.sub(r"\*[^*]+\*", "", text).strip()
    for prefix in ["Assistant:", "Psychologist:"]:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    return text

def build_context():
    return "\n".join(conversation_history[-10:])

def generar_respuesta_con_contexto(user_input):
    conversation_history.append(f"User: {user_input}")

    system_prompt = (
        "You are a licensed clinical psychologist who specializes in cognitive-behavioral therapy. "
        "Your role is to help the user process their emotions, thoughts, and experiences with empathy, care, and without judgment. "
        "Avoid generic advice and explore the user’s emotions with gentle curiosity. Use at least 50 words in your response.\n"
    )

    context = build_context()
    full_prompt = f"{system_prompt}\n{context}\nAssistant:"

    raw = generar_respuesta(full_prompt)

    # Mismo control que tu código original
    if "Assistant:" in raw:
        response = raw.split("Assistant:")[-1]
    else:
        response = raw
    response = response.split("User:")[0].strip()

    response = clean_response(response)
    conversation_history.append(f"Assistant: {response}")
    return response
