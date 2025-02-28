from pydantic import BaseModel
from typing import Optional


class Ayudante(BaseModel):
    id_seccion: int
    id_estudiante: int


class GetEstudiante(BaseModel):
    materia: int
