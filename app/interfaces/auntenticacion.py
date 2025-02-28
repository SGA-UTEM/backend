from pydantic import BaseModel


class Auntenticacion(BaseModel):
    rut: str
    rol: str
