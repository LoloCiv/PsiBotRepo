import smtplib
import os
from email.message import EmailMessage

def enviar_alerta(correo_destino, mensaje_riesgoso):
    gmail_user = os.environ["GMAIL_USER"]
    gmail_password = os.environ["GMAIL_PASSWORD"]

    msg = EmailMessage()
    msg.set_content(f"⚠️ Mensaje riesgoso detectado:\n\n{mensaje_riesgoso}")
    msg["Subject"] = "ALERTA: Mensaje de riesgo"
    msg["From"] = gmail_user
    msg["To"] = correo_destino

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)
        
