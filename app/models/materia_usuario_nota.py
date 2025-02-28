from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class MateriaUsuarioNota(Base):
    __tablename__ = "materias_usuario_notas"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    nota: Mapped[float] = mapped_column(Float, nullable=True)
    estado: Mapped[str] = mapped_column(String, nullable=False)
    id_estudiante: Mapped[int] = mapped_column(
        Integer, ForeignKey("estudiantes.id"), nullable=False
    )
    id_materia: Mapped[int] = mapped_column(
        Integer, ForeignKey("materias.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    estudiante: Mapped["Estudiante"] = relationship(
        "Estudiante", back_populates="materia_usuario_nota"
    )
    materia: Mapped["Materia"] = relationship(
        "Materia", back_populates="materia_usuario_nota"
    )
    postulante: Mapped["Postulante"] = relationship(
        "Postulante", back_populates="materia_usuario_nota"
    )
