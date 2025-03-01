# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
from fastapi import Query

# Interfaces
from app.dependencies import Res
from app.interfaces.reporte import Reporte as ReporteBody

# Services
from app.services.ayudante import ayudante_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/ayudantes",
)
from app.db.db import Session, get_db


@router.get("", response_model=Res[str], tags=["Ayudantes"])
async def recibir_ayudantes(
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:
    ayudantes = ayudante_service.recibir_ayudantes(
        params={"Limit": items_per_page, "Page": page}, db=db
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Ayudantes": ayudantes},
        },
    )


@router.get("/{idMateria}", response_model=Res[str], tags=["Ayudantes"])
async def recibir_ayudantes_materia(
    idMateria: int,
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:
    ayudantes = ayudante_service.recibir_ayudantes_materia(
        method={"materia": idMateria},
        params={"Limit": items_per_page, "Page": page},
        db=db,
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Ayudantes": ayudantes},
        },
    )


@router.post("/reporte", response_model=Res[str], tags=["Ayudantes"])
async def ingresar_reporte(
    content: ReporteBody,
    db: Session = fastapi.Depends(get_db),
) -> Res:
    ayudante_service.crear_reporte(
        reporte=content,
        db=db,
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Message": "Reporte creado con exito"},
        },
    )
