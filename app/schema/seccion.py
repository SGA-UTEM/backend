from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from app.models import Seccion
from app.schema import *


class SeccionSchema(SQLAlchemySchema):
    class Meta:
        model = Seccion
        load_instance = True

    id = auto_field()
    codigo = auto_field()
    materia = fields.Nested(MateriaSchema)
    created_at = auto_field()
