# Responses
import fastapi
from fastapi.exceptions import HTTPException
from app.db.db import Session
from app.schema import *
from app.interfaces.evaluations import Evaluation as EvaluationBody

# Models
from app.models import *

# Interface
from app.interfaces.pagination import Params


status = fastapi.status


class Evaluations:
    def create_evaluation(self, evaluation: EvaluationBody, db: Session) -> dict:
        if evaluation.value != 0 and evaluation.value != 1:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Dato invalido",
            )

        evaluation = Evaluation(
            value=evaluation.value,
            content=evaluation.content,
            id_section=evaluation.id_section,
            id_helper=evaluation.id_helper,
        )
        db.add(evaluation)
        db.commit()
        return

    def get_evaluation_helper(self, id_helper: int, db: Session):
        evaluations = db.query(Evaluation).filter_by(id_helper=id_helper).all()
        if evaluations is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Hubo un error al recibir las evaluaciones del estudiante",
            )
        schema = EvaluationSchema(many=True)
        return schema.dump(evaluations)


evaluations_service = Evaluations()
