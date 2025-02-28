from pydantic import BaseModel
from typing import Optional
from datetime import date


class FechaPostulacion(BaseModel):
    inicio: date
    fin: date


class AsignarFecha(BaseModel):
    id_fecha: int
