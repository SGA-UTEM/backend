from app.utils.emailer.main import initSmtp
from email.message import EmailMessage
from email.mime.image import MIMEImage
import os


def sendEmail(estado: bool, email: str, materia: str, seccion: int):
    smtp = initSmtp()

    # Obtén la ruta absoluta al directorio actual del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construye la ruta completa al archivo de plantilla
    if estado:
        template_path = os.path.join(script_dir, "templates", "aceptada.html")
    else:
        template_path = os.path.join(script_dir, "templates", "rechazada.html")

    try:
        with open(template_path, "r", encoding="utf-8") as file:
            html_template = file.read()
    except FileNotFoundError:
        print("Error: No se pudo encontrar la plantilla HTML.")
        return

    html_content = html_template.format(materia=materia, seccion=seccion)

    em = EmailMessage()
    em["From"] = "Departamento de Informática"
    em["To"] = email
    em["Subject"] = f"Departamento de Informatica - Resultado Solicitud Ayudantia"
    em.add_alternative(html_content, subtype="html")

    images = {
        "header": os.path.join(script_dir, "templates/images", "header.png"),
        "footer": os.path.join(script_dir, "templates/images", "footer.png"),
    }
    for cid, path in images.items():
        try:
            with open(path, "rb") as img:
                img_data = img.read()
                img_attachment = MIMEImage(img_data)
                img_attachment.add_header("Content-ID", f"<{cid}>")
                em.attach(img_attachment)
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar la imagen {path}")
            return
    try:
        smtp.send_message(em)
    finally:
        smtp.quit()
