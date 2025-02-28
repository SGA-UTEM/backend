# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *

status = fastapi.status


class Reportes:
    def recibir_reportes(self, db: Session):
        reportes = db.query(Reporte).all()
        if reportes is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir el reporte",
            )
        schema = ReporteSchema(many=True)
        return schema.dump(reportes)

    def recibir_reportes_ayudante(self, id_ayudante: int, db: Session):
        reportes = db.query(Reporte).filter_by(id_ayudante=id_ayudante).all()
        if reportes is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir la reporte",
            )
        schema = ReporteSchema(many=True)
        return schema.dump(reportes)

    def recibir_reportes_seccion(self, id_seccion: int, db: Session):
        reportes = db.query(Reporte).filter_by(id_seccion=id_seccion).all()
        if reportes is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir la reporte",
            )
        schema = ReporteSchema(many=True)
        return schema.dump(reportes)


reporte_service = Reportes()
