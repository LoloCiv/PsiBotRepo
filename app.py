from flask import Flask, render_template, request, jsonify
from modelo import generar_respuesta
from evaluador import evaluar_mensaje
from correo import enviar_alerta

app = Flask(__name__)

CORREO_ALERTA = "tucorreo@gmail.com"  # CAMBIAR

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.json.get("mensaje", "")
    riesgo = evaluar_mensaje(mensaje_usuario)
    if riesgo == "riesgo":
        enviar_alerta(CORREO_ALERTA, mensaje_usuario)
        return jsonify({"respuesta": "Detecté un mensaje que podría ser peligroso. Te recomiendo buscar ayuda profesional."})
    respuesta = generar_respuesta(mensaje_usuario)
    return jsonify({"respuesta": respuesta})