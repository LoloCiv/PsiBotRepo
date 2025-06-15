from transformers import pipeline

def evaluar_riesgo(mensaje):
    prompt = (
        "You are a sensitive assistant that detects if a message contains suicidal thoughts, self-harm risk, or dangerous behavior.  \n"
        "Respond only with 'risk' or 'safe'.\n\n"
        f"Message: \"{mensaje}\"\n\n"
        "Response:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=10,
        pad_token_id=tokenizer.eos_token_id,
    )
    respuesta = tokenizer.decode(output[0], skip_special_tokens=True)
    respuesta_final = respuesta[len(prompt):].strip().lower()

    if respuesta_final.startswith("risk"):
        return "risk"
    else:
        return "safe"
