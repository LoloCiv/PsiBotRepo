import os
from flask import Flask, render_template, request, jsonify
from respuesta import generar_respuesta_con_contexto
from evaluador import evaluar_mensaje
from correo import enviar_alerta

app = Flask(__name__)
CORREO_ALERTA = "laureanocivetta@gmail.com"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.json.get("mensaje", "")

    # Evaluar si el mensaje es riesgoso
    riesgo = evaluar_mensaje(mensaje_usuario)
    if riesgo == "riesgo":
        enviar_alerta(CORREO_ALERTA, mensaje_usuario)
        return jsonify({
            "respuesta": "Detecté un mensaje que podría ser peligroso. Te recomiendo buscar ayuda profesional."
        })

    # Generar respuesta con historial y prompt psicológico
    respuesta = generar_respuesta_con_contexto(mensaje_usuario)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
