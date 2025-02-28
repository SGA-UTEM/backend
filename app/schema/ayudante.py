from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import Ayudante
from app.schema import *
from marshmallow_sqlalchemy.fields import Nested


class AyudanteSchema(SQLAlchemySchema):
    class Meta:
        model = Ayudante
        load_instance = True

    id = auto_field()
    estudiante = Nested(EstudianteSchema)
    seccion = Nested(SeccionSchema)
    created_at = auto_field()
