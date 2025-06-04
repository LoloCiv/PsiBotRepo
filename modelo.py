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

def generar_respuesta(mensaje):
    input_ids = tokenizer(mensaje, return_tensors="pt").input_ids.to(device)
    output = model.generate(input_ids, max_new_tokens=200)
    return tokenizer.decode(output[0], skip_special_tokens=True)