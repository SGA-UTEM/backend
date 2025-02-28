# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from fastapi import Query
from app.interfaces.fecha_postulacion import FechaPostulacion, AsignarFecha

# Services
from app.services.fecha_postulacion import fechas_postulacion_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/fecha_postulacion",
)
from app.db.db import Session, get_db


@router.post(
    "",
    response_model=Res[str],
)
async def crear_fecha_postuacion(
    fecha: FechaPostulacion, db: Session = fastapi.Depends(get_db)
) -> Res:
    fechas_postulacion_service.crear_fecha_postulacion(fecha=fecha, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Message": "La fecha de postulacion fue creada con exito"},
        },
    )


@router.get(
    "",
    response_model=Res[str],
)
async def recibir_fechas_postulacion(db: Session = fastapi.Depends(get_db)) -> Res:
    fechas = fechas_postulacion_service.recibir_fechas_postulacion(db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Fechas Postulacion": fechas},
        },
    )


@router.post(
    "/asignar",
    response_model=Res[str],
)
async def asignar_fecha(
    id_fecha: AsignarFecha, db: Session = fastapi.Depends(get_db)
) -> Res:
    fechas_postulacion_service.asignar_fecha(id_fecha=id_fecha, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Message": "Fecha asignada con exito"},
        },
    )
