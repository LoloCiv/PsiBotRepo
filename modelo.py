from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

model_name = "meta-llama/Llama-2-7b-chat-hf"

quant_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

def generar_respuesta(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(model.device)
    
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

""" 
def generar_respuesta_evaluador(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=10,
        pad_token_id=tokenizer.eos_token_id,
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
"""

def generar_respuesta_evaluador(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)  # sin .to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=5,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=False,
        num_beams=5,
        early_stopping=True,
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
