from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from marshmallow_sqlalchemy.fields import Nested
from app.models import MateriaUsuarioNota
from app.schema import *


class MateriaUsuarioNotaSchema(SQLAlchemySchema):
    class Meta:
        model = MateriaUsuarioNota
        load_instance = True

    id = auto_field()
    nota = auto_field()
    estado = auto_field()
    estudiante = Nested(EstudianteSchema)
    materia = Nested(MateriaSchema)
    created_at = auto_field()
