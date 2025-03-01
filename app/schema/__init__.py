from .estudiante import EstudianteSchema
from .materia import MateriaSchema
from .materia_usuario_nota import MateriaUsuarioNotaSchema
from .postulantes import PostulanteSchema
from .seccion import SeccionSchema
from .ayudante import AyudanteSchema
from .reportes import ReporteSchema
from .fecha_postulacion import FechaPostulacionSchema
from .evaluation import EvaluationSchema

__all__ = [
    "EstudianteSchema",
    "MateriaSchema",
    "MateriaUsuarioNotaSchema",
    "SeccionSchema",
    "PostulanteSchema",
    "AyudanteSchema",
    "ReporteSchema",
    "FechaPostulacionSchema",
    "EvaluationSchema",
]
