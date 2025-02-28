from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from app.models import Materia


class MateriaSchema(SQLAlchemySchema):
    class Meta:
        model = Materia
        load_instance = True

    id = auto_field()
    nombre = auto_field()
    id_departamento = auto_field()
    created_at = auto_field()
