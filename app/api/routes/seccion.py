# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res

# Services
from app.services.secciones import seccion_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/secciones",
)
from app.db.db import Session, get_db


@router.get("/{idMateria}", response_model=Res[str], tags=["Seccion"])
async def recibir_postulaciones(
    idMateria: int,
    db: Session = fastapi.Depends(get_db),
) -> Res:
    seccion = seccion_service.get_seccion(id=idMateria, db=db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": {"Seccion": seccion},
        },
    )
