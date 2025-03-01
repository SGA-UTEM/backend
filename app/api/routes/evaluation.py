# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from app.interfaces.evaluations import Evaluation

# Services
from app.services.evaluations import evaluations_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/evaluations",
)
from app.db.db import Session, get_db


@router.post("", response_model=Res[str], tags=["Evaluaciones Ayudante"])
async def create_evaluation(
    evaluation: Evaluation, db: Session = fastapi.Depends(get_db)
) -> Res:
    evaluations_service.create_evaluation(evaluation=evaluation, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "message": "Evaluacion al ayudante hecha con exito",
        },
    )


@router.get("/{id_helper}", response_model=Res[str], tags=["Evaluaciones Ayudante"])
async def get_evaluation(id_helper: int, db: Session = fastapi.Depends(get_db)) -> Res:
    evaluations = evaluations_service.get_evaluation_helper(id_helper=id_helper, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": evaluations,
        },
    )
