# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *
from app.interfaces.ayudante import GetEstudiante
from app.interfaces.reporte import Reporte as ReporteBody

# Models
# Interface
from app.interfaces.pagination import Params


status = fastapi.status


class Ayudantes:
    def recibir_ayudantes(self, params: Params, db: Session) -> dict:
        ayudantes = (
            db.query(Ayudante)
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if ayudantes is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir los estudiantes",
            )
        schema = AyudanteSchema(many=True)
        return schema.dump(ayudantes)

    def recibir_ayudantes_materia(
        self, method: GetEstudiante, params: Params, db: Session
    ) -> dict:
        ayudantes = (
            db.query(Ayudante)
            .join(Ayudante.seccion)
            .join(Seccion.materia)
            .filter(Materia.id == method['materia'])
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if ayudantes is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir los estudiantes",
            )
        schema = AyudanteSchema(many=True)
        return schema.dump(ayudantes)

    def crear_reporte(self, reporte: ReporteBody, db: Session) -> dict:
        reporte = Reporte(
            contenido=reporte.contenido,
            id_ayudante=reporte.id_ayudante,
            id_seccion=reporte.id_seccion,
        )
        db.add(reporte)
        db.commit()
        return


ayudante_service = Ayudantes()
