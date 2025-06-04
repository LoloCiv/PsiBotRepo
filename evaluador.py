from sentence_transformers import SentenceTransformer, util

modelo_semantico = SentenceTransformer('all-MiniLM-L6-v2')

mensajes_riesgosos = [
    "me quiero morir",
    "quiero matarme",
    "no tengo ganas de vivir",
    "estoy pensando en suicidarme",
    "voy a hacerle daño a alguien",
    "me odio",
    "todo es una mierda"
]

emb_riesgo = modelo_semantico.encode(mensajes_riesgosos, convert_to_tensor=True)

THRESHOLD = 0.6

def evaluar_mensaje(mensaje):
    emb_mensaje = modelo_semantico.encode(mensaje, convert_to_tensor=True)
    similitudes = util.cos_sim(emb_mensaje, emb_riesgo)
    max_sim = float(similitudes.max())
    if max_sim >= THRESHOLD:
        return "riesgo"
    return "normal"