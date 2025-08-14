from email_service import enviar_email

if __name__ == "__main__":
    enviar_email(
        destinatario="destino@gmail.com",
        assunto="Teste Automático",
        corpo="Este é um e-mail enviado automaticamente com Python."
    )
