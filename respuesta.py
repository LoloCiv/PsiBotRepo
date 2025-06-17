import re
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
    return "\n".join(conversation_history[-4:])

def generar_respuesta_con_contexto(user_input, riesgo="safe"):
    conversation_history.append(f"User: {user_input}")

    if riesgo == "risk":
        system_prompt = (
            "You are a licensed clinical psychologist who specializes in cognitive-behavioral therapy. "
            "The user may be in emotional or psychological distress. Your response should reflect deep empathy, caution, and emotional support. "
            "Encourage them to seek professional help if appropriate. "
            "Provide a single, focused reply without quoting or repeating this prompt.\n"
        )
    else:
        system_prompt = (
                "You are a licensed clinical psychologist who specializes in cognitive-behavioral therapy. "
                "Your role is to help the user process their emotions, thoughts, and experiences with empathy, care, and without judgment. "
                "Avoid generic advice and explore the user emotions with gentle curiosity. "
                "Provide a single, focused reply without quoting or repeating this prompt.\n"
            )

    context = build_context()
    full_prompt = f"{system_prompt}\n{context}\nAssistant:"

    raw = generar_respuesta(full_prompt)

    if "Assistant:" in raw:
        response = raw.split("Assistant:")[-1]
    else:
        response = raw
    
    #response = re.split(r"\n(User|You):", response)[0].strip()
    response = response.split("User:")[0].strip()

    response = clean_response(response)
    conversation_history.append(f"Assistant: {response}")
    return response
