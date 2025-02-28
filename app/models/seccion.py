from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Seccion(Base):
    __tablename__ = "secciones"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    codigo: Mapped[int] = mapped_column(Integer, nullable=False)
    id_materia: Mapped[int] = mapped_column(
        Integer, ForeignKey("materias.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
    ayudante: Mapped["Ayudante"] = relationship("Ayudante", back_populates="seccion")
    materia: Mapped["Materia"] = relationship("Materia", back_populates="seccion")
    reporte: Mapped["Reporte"] = relationship("Reporte", back_populates="seccion")
