from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from app.models import Reporte
from app.schema import *


class ReporteSchema(SQLAlchemySchema):
    class Meta:
        model = Reporte
        load_instance = True

    id = auto_field()
    id_ayudante = auto_field()
    contenido = auto_field()
    seccion = fields.Nested(SeccionSchema)
    created_at = auto_field()
