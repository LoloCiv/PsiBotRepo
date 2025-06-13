!pip install flask pyngrok

from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok
import threading
import os

from respuesta import generar_respuesta_con_contexto  # ✅ Nuevo
from evaluador import evaluar_mensaje
from correo import enviar_alerta

# Config Flask
app = Flask(__name__, template_folder='templates')
CORREO_ALERTA = "laureanocivetta@gmail.com"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.json.get("mensaje", "")

    # Evaluar si es un mensaje riesgoso
    riesgo = evaluar_mensaje(mensaje_usuario)
    if riesgo == "riesgo":
        enviar_alerta(CORREO_ALERTA, mensaje_usuario)
        return jsonify({
            "respuesta": "Detecté un mensaje que podría ser peligroso. Te recomiendo buscar ayuda profesional."
        })

    # Generar respuesta con historial y prompt especializado
    respuesta = generar_respuesta_con_contexto(mensaje_usuario)
    return jsonify({"respuesta": respuesta})

# Ejecutar Flask en segundo plano
def run_app():
    app.run(port=8000)

thread = threading.Thread(target=run_app)
thread.start()

# Crear túnel ngrok
public_url = ngrok.connect(8000)
print(f"✔️ Chatbot disponible en: {public_url}")
