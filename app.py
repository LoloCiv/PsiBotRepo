from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok
import threading

from respuesta import generar_respuesta_con_contexto
from evaluador import evaluar_mensaje
from correo import enviar_alerta

app = Flask(__name__, template_folder='templates')
CORREO_ALERTA = "laureanocivetta@gmail.com"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.json.get("mensaje", "")

    try:
        riesgo = evaluar_mensaje(mensaje_usuario)
    except Exception as e:
        print(f"Error evaluando riesgo: {e}")
        riesgo = "normal"

    if riesgo == "risk":  # Ajusta esto según el output de tu evaluador
        threading.Thread(target=enviar_alerta, args=(CORREO_ALERTA, mensaje_usuario)).start()
        return jsonify({
            "respuesta": "Detecté un mensaje que podría ser peligroso. Te recomiendo buscar ayuda profesional."
        })

    respuesta = generar_respuesta_con_contexto(mensaje_usuario)
    return jsonify({"respuesta": respuesta})

def run_app():
    app.run(host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_app)
thread.start()

public_url = ngrok.connect(8000)
print(f"✔️ Chatbot disponible en: {public_url}")
