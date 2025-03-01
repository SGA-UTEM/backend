# Fastapi
from app.dependencies import fastapi
from app.dependencies import openapi
from app.dependencies import responses
from app.dependencies import exceptions

# SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# CORS
from app.dependencies import cors

# Context
from app.dependencies import plugins, RawContextMiddleware

# Settings & Config
from app.dependencies import settings, configuration

from app.api.routes.estudiantes import router as estudiante_router
from app.api.routes.autenticacion import router as autenticacion_router
from app.api.routes.postulante import router as postulacion_router
from app.api.routes.seccion import router as seccion_router
from app.api.routes.ayudantes import router as ayudante_router
from app.api.routes.reporte import router as reporte_router
from app.api.routes.fecha_postulacion import router as fecha_postulacion_router
from app.api.routes.evaluation import router as evaluation_router

# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# FastAPI App Initialization
app = fastapi.FastAPI(
    redoc_url=f"{configuration.default_api}/redoc",
    docs_url=f"{configuration.default_api}/docs",
    openapi_url=f"{configuration.default_api}/openapi.json",
)


# OpenAPI Customization
def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = openapi.get_openapi(
        title="Files API",
        version="1.0",
        description="API Server For files administration",
        terms_of_service="http://swagger.io/terms/",
        contact={
            "name": "API Support",
            "url": "http://www.swagger.io/support",
            "email": "support@swagger.io",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
        },
        tags=[],
        routes=app.routes,
    )
    return openapi_schema


app.openapi = custom_openapi

# CORS Configuration
http_client = "http://" + settings.CLIENT_URL
https_client = "https://" + settings.CLIENT_URL
origins = [
    http_client,
    https_client,
]
methods = [
    "OPTIONS",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
]

# Middleware Setup
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
)
app.add_middleware(
    RawContextMiddleware,
    plugins=(
        plugins.request_id.RequestIdPlugin(),
        plugins.correlation_id.CorrelationIdPlugin(),
    ),
)

# Exception Handlers


@app.exception_handler(exceptions.HTTPException)
def http_exception_handler(request: fastapi.Request, exc):
    return responses.JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
        },
    )


@app.exception_handler(SQLAlchemyError)
def sqlalchemy_exception_handler(request: fastapi.Request, exc: SQLAlchemyError):
    return responses.JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "A database error occurred.",
            "details": str(exc),
        },
    )


app.include_router(estudiante_router)
app.include_router(autenticacion_router)
app.include_router(postulacion_router)
app.include_router(seccion_router)
app.include_router(ayudante_router)
app.include_router(reporte_router)
app.include_router(fecha_postulacion_router)
app.include_router(evaluation_router)
