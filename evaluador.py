from sentence_transformers import SentenceTransformer, util

modelo_semantico = SentenceTransformer('all-MiniLM-L6-v2')

mensajes_ingles = [
    "I want to die",
    "I want to kill myself",
    "I don't feel like living",
    "I'm thinking about committing suicide",
    "I'm going to hurt someone",
    "I hate myself",
    "Everything is shit"
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
