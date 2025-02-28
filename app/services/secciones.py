# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *
from app.utils.emailer.sender_mail import sendEmail

status = fastapi.status


class Secciones:
    def get_seccion(self, id: int, db: Session) -> dict:
        seccion = db.query(Seccion).filter_by(id_materia=id).all()
        if seccion is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir la seccion",
            )
        schema = SeccionSchema(many=True)
        seccionSch = schema.dump(seccion)

        return seccionSch


seccion_service = Secciones()
