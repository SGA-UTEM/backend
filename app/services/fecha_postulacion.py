# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *
from datetime import date
from app.interfaces.fecha_postulacion import (
    AsignarFecha,
    FechaPostulacion as FechaPostulacionBody,
)

status = fastapi.status


class FechasPostulaciones:
    def crear_fecha_postulacion(self, fecha: FechaPostulacionBody, db: Session):
        fechaPostulacion = FechaPostulacion(inicio=fecha.inicio, fin=fecha.fin)
        db.add(fechaPostulacion)

        db.commit()
        return

    def recibir_fechas_postulacion(self, db: Session):
        fechas_postulacion = db.query(FechaPostulacion).all()
        if fechas_postulacion is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir las fechas_postulacion",
            )
        schema = FechaPostulacionSchema(many=True)
        return schema.dump(fechas_postulacion)

    def asignar_fecha(self, id_fecha: AsignarFecha, db: Session):
        fecha = db.query(FechaPostulacion).filter_by(id=id_fecha.id_fecha).first()
        if fecha is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir la fecha",
            )
        fechaAsignada = db.query(FechaPostulacion).filter_by(is_asigned=True).first()
        if fechaAsignada is not None:
            fechaAsignada.is_asigned = False

        fecha.is_asigned = True
        db.commit()
        return

    def recibir_fecha_asignada(self, db: Session):
        fecha = db.query(FechaPostulacion).filter_by(is_asigned=True).first()
        if fecha is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir la fecha",
            )

        return fecha

    def comprobar_fecha_en_rango(self, fecha_actual: date, db: Session):
        fecha = self.recibir_fecha_asignada(db)

        return fecha.inicio.date() <= fecha_actual <= fecha.fin.date()


fechas_postulacion_service = FechasPostulaciones()
