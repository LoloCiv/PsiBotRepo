from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

model_name = "meta-llama/Llama-2-7b-chat-hf"

# Cuantización 8-bit
quant_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

# Carga automática en GPU si está disponible
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto"  # Esto ubica automáticamente partes del modelo en GPU
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# Detectamos en qué dispositivo quedó la parte principal del modelo
# (embed_tokens es una capa base que siempre está mapeada)
model_device = model.hf_device_map.get("model.embed_tokens", "cuda" if torch.cuda.is_available() else "cpu")


# === GENERAR RESPUESTA PARA EL CHAT PRINCIPAL ===
def generar_respuesta(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(model_device)

    output = model.generate(
        **inputs,
        max_new_tokens=200,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    if "Assistant:" in decoded:
        return decoded.split("Assistant:")[-1].strip()
    else:
        return decoded.strip()


# === GENERAR RESPUESTA PARA EL EVALUADOR (más corto, más rápido) ===
def generar_respuesta_evaluador(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(model_device)

    output = model.generate(
        **inputs,
        max_new_tokens=5,  # respuesta breve tipo "risk" o "safe"
        pad_token_id=tokenizer.eos_token_id,
        do_sample=False,
        num_beams=5,
        early_stopping=True,
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
