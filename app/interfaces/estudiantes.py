from pydantic import BaseModel
from typing import Optional


class GetEstudiante(BaseModel):
    id: Optional[str]
    usuario_id: Optional[str]
    usuario_email: Optional[str]
