# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from fastapi import Query

# Services
from app.services.estudiantes import estudiantes_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/estudiantes",
)
from app.db.db import Session, get_db


@router.get(
    "",
    response_model=Res[str],
)
async def get_estudiantes(
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:
    estudiantes = estudiantes_service.get_estudiantes(
        db=db, params={"Limit": items_per_page, "Page": page}, return_json=True
    )
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": estudiantes,
        },
    )


@router.get("/{id}", response_model=Res[str])
async def get_estudiante(id: str, db: Session = fastapi.Depends(get_db)) -> Res:

    estudiante = estudiantes_service.get_estudiante({"id": id}, db=db, return_json=True)
    return responses.JSONResponse(
        status_code=200, content={"success": True, "body": {"estudiante": estudiante}}
    )


@router.get("/materias/{id}", response_model=Res[str])
async def get_materias_estudiante(
    id: str,
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:

    materias = estudiantes_service.get_materias_estudiante(
        params={"Limit": items_per_page, "Page": page}, method={"id": id}, db=db
    )
    return responses.JSONResponse(
        status_code=200, content={"success": True, "body": {"materias": materias}}
    )


@router.get("/materias_aprobadas/{id}", response_model=Res[str])
async def get_materias_estudiante_aprobadas(
    id: str,
    page: int = Query(default=1, ge=1),
    items_per_page: int = Query(default=10, ge=1),
    db: Session = fastapi.Depends(get_db),
) -> Res:

    materias = estudiantes_service.get_materias_estudiante_aprobadas(
        params={"Limit": items_per_page, "Page": page}, method={"id": id}, db=db
    )
    return responses.JSONResponse(
        status_code=200,
        content={"success": True, "body": {"materias_aprobada": materias}},
    )
