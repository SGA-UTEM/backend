from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import Estudiante
from app.schema import *
from marshmallow_sqlalchemy.fields import Nested


class EstudianteSchema(SQLAlchemySchema):
    class Meta:
        model = Estudiante
        load_instance = True

    id = auto_field()
    rut = auto_field()
    nombre = auto_field()
    email = auto_field()
    estudiante_regular = auto_field()
    created_at = auto_field()
