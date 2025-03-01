# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from app.interfaces.auntenticacion import Auntenticacion

# Services
from app.services.auntenticacion import auntenticacion_service

# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f"{configuration.default_api}/auntenticacion",
)
from app.db.db import Session, get_db


@router.post("", response_model=Res[str], tags=["Auntenticacion"])
async def inicio_sesion(
    auth: Auntenticacion, db: Session = fastapi.Depends(get_db)
) -> Res:
    usuario = auntenticacion_service.auntenticacion(auth, db)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "body": usuario,
        },
    )
