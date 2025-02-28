# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.models import *
from sqlalchemy import and_

from app.interfaces.estudiantes import GetEstudiante
from app.interfaces.pagination import Params

status = fastapi.status


class Estudiantes:
    def get_estudiante(
        self, method: GetEstudiante, db: Session, return_json=False
    ) -> Estudiante:
        if "id" in method:
            if return_json:
                user = db.query(Estudiante).filter_by(id == method["id"]).first()

                schema = EstudianteSchema()
                return schema.dump(user)

    def get_estudiantes(
        self, db: Session, params: Params, return_json=False
    ) -> Estudiante:
        users = (
            db.query(Estudiante)
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if users is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir los estudiantes",
            )

        if return_json:
            schema = EstudianteSchema(many=True)
            return schema.dump(users)
        return users

    def get_materias_estudiante(
        self, params: Params, method: GetEstudiante, db: Session
    ):
        materias = (
            db.query(MateriaUsuarioNota)
            .filter_by(id_estudiante=method["id"])
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if materias is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                deletail="Hubo un error al recibir las materias del estudiante",
            )
        schema = MateriaUsuarioNotaSchema(many=True)
        return schema.dump(materias)

    def get_materias_estudiante_aprobadas(
        self, params: Params, method: GetEstudiante, db: Session
    ):
        materias = (
            db.query(MateriaUsuarioNota)
            .filter(
                and_(
                    MateriaUsuarioNota.id_estudiante == method["id"],
                    MateriaUsuarioNota.estado == "aprobado",
                )
            )
            .limit(params["Limit"])
            .offset((params["Page"] - 1) * params["Limit"])
            .all()
        )
        if materias is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                deletail="Hubo un error al recibir las materias del estudiante",
            )
        schema = MateriaUsuarioNotaSchema(many=True)
        return schema.dump(materias)


estudiantes_service = Estudiantes()
