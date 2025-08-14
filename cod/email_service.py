import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def enviar_email(destinatario, assunto, corpo):
    remetente = os.getenv("EMAIL_REMETENTE")
    senha = os.getenv("EMAIL_SENHA")
    servidor_smtp = os.getenv("SMTP_SERVIDOR")
    porta = int(os.getenv("SMTP_PORTA"))

    try:
        msg = MIMEMultipart()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = assunto
        msg.attach(MIMEText(corpo, "plain"))

        with smtplib.SMTP(servidor_smtp, porta) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
        print("✅ Email enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")
