

"""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

BASE_MODEL_ID = "meta-llama/Llama-2-7b-chat-hf"
FINETUNED_PATH = "./llama2_finetuned"  # Pon None si no usas LoRA

quant_config = BitsAndBytesConfig(
    load_in_8bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16,
    llm_int8_enable_fp32_cpu_offload=True,
)

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_ID,
    quantization_config=quant_config,
    device_map="auto",
    torch_dtype=torch.float16,
)

model = PeftModel.from_pretrained(base_model, FINETUNED_PATH) if FINETUNED_PATH else base_model
tokenizer = AutoTokenizer.from_pretrained(FINETUNED_PATH or BASE_MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token

DEVICE = next(model.parameters()).device

def generar_respuesta_modelo(prompt: str, max_new_tokens: int = 300, temperature: float = 0.5, top_p: float = 0.85) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(DEVICE)
    output = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
"""
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

model_name = "meta-llama/Llama-2-7b-chat-hf"

quant_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

model_device = model.hf_device_map.get("model.embed_tokens", "cuda" if torch.cuda.is_available() else "cpu")

def generar_respuesta(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(model_device)

    output = model.generate(
        **inputs,
        max_new_tokens=200,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.85
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    if "Assistant:" in decoded:
        return decoded.split("Assistant:")[-1].strip()
    return decoded.strip()
