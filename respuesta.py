def build_context():
    # construir conversación en formato de chat model
    # Ejemplo:
    context = ""
    for turn in conversation_history[-10:]:
        if turn.startswith("User:"):
            context += f"\nUser: {turn[len('User: '):]}"
        elif turn.startswith("Assistant:"):
            context += f"\nAssistant: {turn[len('Assistant: '):]}"
    return context

def generar_respuesta_con_contexto(user_input):
    system_prompt = (
        "You are a licensed clinical psychologist who specializes in cognitive-behavioral therapy. "
        "Your role is to help the user process their emotions, thoughts, and experiences with empathy, care, and without judgment. "
        "Avoid generic advice and explore the user’s emotions with gentle curiosity. Use at least 50 words in your response."
    )
    
    conversation_history.append(f"User: {user_input}")
    
    context = build_context()
    
    full_prompt = f"<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>{context}\nAssistant:"
    
    response = generar_respuesta(full_prompt)
    
    conversation_history.append(f"Assistant: {response}")
    
    return response
