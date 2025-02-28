from pydantic import BaseModel
from typing import Optional


class Reporte(BaseModel):
    id_ayudante: int
    id_seccion: int
    contenido: str
