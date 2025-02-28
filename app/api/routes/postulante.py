# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from app.interfaces.postulante import PostulanteBody, EstadoPostulacion
from fastapi import Query

# Services
from app.services.postulante import postulante_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/postulantes",
)
from app.db.db import Session, get_db


@router.post(
    "",
    response_model=Res[str],
)
async def postular_ayundatias(
    postulante: PostulanteBody, db: Session = fastapi.Depends(get_db)
) -> Res:
    postulante_service.postular_ayudantias(postulante, db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Message": "Postulacion con exito"},
        },
    )


@router.get(
    "",
    response_model=Res[str],
)
async def recibir_postulaciones(
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:
    postulaciones = postulante_service.recibir_postulaciones(
        params={"Limit": items_per_page, "Page": page}, db=db
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Postulaciones": postulaciones},
        },
    )


@router.post(
    "/interactuar",
    response_model=Res[str],
)
async def interactuar_postulacion(
    estado_postulacion: EstadoPostulacion,
    db: Session = fastapi.Depends(get_db),
) -> Res:
    postulaciones = postulante_service.interactuar_postulacion(
        estado_postulacion=estado_postulacion, db=db
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
        },
    )
