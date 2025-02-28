from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from app.models import Postulante
from app.schema import *


class PostulanteSchema(SQLAlchemySchema):
    class Meta:
        model = Postulante
        load_instance = True

    id = auto_field()
    prioridad = auto_field()
    materia_usuario_nota = fields.Nested(MateriaUsuarioNotaSchema)
    created_at = auto_field()
