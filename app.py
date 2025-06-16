from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok, conf
import threading

from respuesta import generar_respuesta_con_contexto
from evaluador import evaluar_mensaje
from correo import enviar_alerta

# ✅ Autenticación con Ngrok
conf.get_default().auth_token = "2y3W36wyqQbDOUiz4H5tXPbVhhW_RkBGXd1iTFByQH5wQtx6"

app = Flask(__name__, static_folder="static", template_folder="templates")
CORREO_ALERTA = "laureanocivetta@gmail.com"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.json.get("mensaje", "").strip()

    if not mensaje_usuario:
        return jsonify({"error": "No message provided"}), 400

    try:
        riesgo = evaluar_mensaje(mensaje_usuario)
    except Exception as e:
        print(f"Error evaluando riesgo: {e}")
        riesgo = "safe"

    # Enviar alerta si hay riesgo
    if riesgo == "risk":
        threading.Thread(target=enviar_alerta, args=(CORREO_ALERTA, mensaje_usuario)).start()

    # Generar respuesta con contexto, indicando si hay riesgo
    respuesta = generar_respuesta_con_contexto(mensaje_usuario, riesgo=riesgo)
    return jsonify({"respuesta": respuesta})

def run_app():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    thread = threading.Thread(target=run_app)
    thread.start()

    public_url = ngrok.connect(8000)
    print(f"✔️ Chatbot disponible en: {public_url}")
