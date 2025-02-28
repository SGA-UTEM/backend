# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *

# Models
# Interface
from app.interfaces.postulante import PostulanteBody, EstadoPostulacion
from app.interfaces.pagination import Params

from app.utils.emailer.sender_mail import sendEmail

status = fastapi.status


class Postulacion:
    def postular_ayudantias(self, postulante: PostulanteBody, db: Session) -> dict:

        for i, pos in enumerate(postulante.materiaUN):
            postulacion = Postulante(prioridad=i + 1, id_materia_usuario_nota=pos)
            db.add(postulacion)

        db.commit()
        return

    def recibir_postulaciones(self, params: Params, db: Session):
        postulaciones = (
            db.query(Postulante)
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if postulaciones is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir las postulaciones",
            )
        schema = PostulanteSchema(many=True)
        postulaciones = schema.dump(postulaciones)
        postul = {}
        for i in postulaciones:
            usuario_id = i["materia_usuario_nota"]["estudiante"]["id"]
            materia = {
                "id": i["materia_usuario_nota"]["id"],
                "id_postulacion": i["id"],
                "nota": i["materia_usuario_nota"]["nota"],
                "materia": i["materia_usuario_nota"]["materia"],
            }
            if usuario_id not in postul:
                postul[usuario_id] = {"usuario_id": usuario_id, "materias": []}
            postul[usuario_id]["materias"].append(materia)

        return list(postul.values())

    def interactuar_postulacion(
        self, estado_postulacion: EstadoPostulacion, db: Session
    ):
        postulacion = db.query(Postulante).filter_by(id=estado_postulacion.id).first()
        if estado_postulacion.estado and estado_postulacion.id_seccion is not None:
            ayudante = Ayudante(
                id_estudiante=postulacion.materia_usuario_nota.estudiante.id,
                id_seccion=estado_postulacion.id_seccion,
            )
            db.add(ayudante)

            sendEmail(
                estado_postulacion.estado,
                postulacion.materia_usuario_nota.estudiante.email,
                postulacion.materia_usuario_nota.materia.nombre,
                estado_postulacion.id_seccion,
            )

            db.delete(postulacion)
        elif estado_postulacion.estado == False:

            sendEmail(
                estado_postulacion.estado,
                postulacion.materia_usuario_nota.estudiante.email,
                postulacion.materia_usuario_nota.materia.nombre,
                estado_postulacion.id_seccion,
            )
            db.delete(postulacion)

        db.commit()
        return


postulante_service = Postulacion()
