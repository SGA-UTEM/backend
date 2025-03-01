from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import Evaluation
from app.schema import *
from marshmallow_sqlalchemy.fields import Nested


class EvaluationSchema(SQLAlchemySchema):
    class Meta:
        model = Evaluation
        load_instance = True

    id = auto_field()
    value = auto_field()
    content = auto_field()
    id_section = auto_field()
    helper = Nested(AyudanteSchema)
    created_at = auto_field()
