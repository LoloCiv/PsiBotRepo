import smtplib
from email.message import EmailMessage

def enviar_alerta(correo_destino, mensaje_riesgoso):
    msg = EmailMessage()
    msg.set_content(f"⚠️ Mensaje riesgoso detectado:\n\n{mensaje_riesgoso}")
    msg["Subject"] = "ALERTA: Mensaje de riesgo"
    msg["From"] = "laureanocivetta@gmail.com" 
    msg["To"] = correo_destino

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("laureanocivetta@gmail.com", "otwn gqja hklb ngyc")  
        smtp.send_message(msg)