from pydantic import BaseModel
from typing import Optional


class Postulante(BaseModel):
    prioridad: int
    id_materia_usuario_nota: int

    def to_model(self):
        return {
            "prioridad": self.prioridad,
            "id_materia_usuario_nota": self.id_materia_usuario_nota,
        }


class PostulanteBody(BaseModel):
    materiaUN: list[int]


class EstadoPostulacion(BaseModel):
    id: int
    estado: bool
    id_seccion: Optional[int]
