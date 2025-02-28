import os
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()


def initSmtp():
    context = ssl.create_default_context()

    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        smtp.login(os.getenv("SENDER_EMAIL"), os.getenv("PASSWORD_EMAILER"))
    except Exception as e:
        print(f"Error al conectar con el servidor SMTP: {e}")
    return smtp
