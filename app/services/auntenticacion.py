# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *

from datetime import date

# Interface
from app.interfaces.auntenticacion import Auntenticacion
from app.interfaces.tipos_usuarios import TiposUsuarios

from app.services.fecha_postulacion import fechas_postulacion_service

status = fastapi.status


class Auntenticacion:
    def auntenticacion(self, auth: Auntenticacion, db: Session) -> dict:

        if auth.rol == TiposUsuarios.ESTUDIANTE.value:
            user = db.query(Estudiante).filter_by(rut=auth.rut).first()

            fecha = fechas_postulacion_service.comprobar_fecha_en_rango(
                fecha_actual=date.today(), db=db
            )
            print(fecha)
            if fecha is False:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Todavia no se puede postular",
                )

            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Hubo un error al auntenticar al estudiante",
                )
            if user.estudiante_regular == False:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="El estudiante no es alumno regular",
                )
            return {"Usuario": user.id}

        if auth.rol == TiposUsuarios.DIRECTOR.value:
            user = db.query(Director).filter_by(rut=auth.rut).first()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Hubo un error al auntenticar al director",
                )
            return {"Usuario": user.id}
        if auth.rol == TiposUsuarios.CORDINADOR.value:
            user = db.query(Cordinador).filter_by(rut=auth.rut).first()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Hubo un error al auntenticar al cordinador",
                )
            return {"Usuario": user.id}

        if auth.rol == TiposUsuarios.AYUDANTE.value:
            user = (
                db.query(Ayudante)
                .join(Ayudante.estudiante)
                .filter(Ayudante.estudiante.has(rut=auth.rut))
                .first()
            )
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Hubo un error al auntenticar al Ayudante",
                )
            return {"Usuario": user.id}


auntenticacion_service = Auntenticacion()
