# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res

# Services
from app.services.reportes import reporte_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/reportes",
)
from app.db.db import Session, get_db


@router.get("/ayudante/{id_ayudante}", response_model=Res[str], tags=["Reportes"])
async def recibir_reportes_ayudante(
    id_ayudante: int,
    db: Session = fastapi.Depends(get_db),
) -> Res:
    reporte = reporte_service.recibir_reportes_ayudante(id_ayudante=id_ayudante, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Reportes": reporte},
        },
    )


@router.get("/seccion/{id_seccion}", response_model=Res[str], tags=["Reportes"])
async def recibir_reportes_seccion(
    id_seccion: int,
    db: Session = fastapi.Depends(get_db),
) -> Res:
    reportes = reporte_service.recibir_reportes_seccion(id_seccion=id_seccion, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Reportes": reportes},
        },
    )


@router.get("", response_model=Res[str], tags=["Reportes"])
async def recibir_reportes(
    db: Session = fastapi.Depends(get_db),
) -> Res:
    reportes = reporte_service.recibir_reportes(db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Reportes": reportes},
        },
    )
