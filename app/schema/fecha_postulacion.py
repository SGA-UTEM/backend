from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from app.models import FechaPostulacion


class FechaPostulacionSchema(SQLAlchemySchema):
    class Meta:
        model = FechaPostulacion
        load_instance = True

    id = auto_field()
    inicio = auto_field()
    fin = auto_field()
    is_asigned = auto_field()
    created_at = auto_field()
