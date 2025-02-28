from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Ayudante(Base):
    __tablename__ = "ayudantes"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    id_estudiante: Mapped[int] = mapped_column(
        Integer, ForeignKey("estudiantes.id"), nullable=False
    )
    id_seccion: Mapped[int] = mapped_column(
        Integer, ForeignKey("secciones.id"), nullable=False
    )

    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    estudiante: Mapped["Estudiante"] = relationship(
        "Estudiante", back_populates="ayudante"
    )
    seccion: Mapped["Seccion"] = relationship("Seccion", back_populates="ayudante")
    reporte: Mapped["Reporte"] = relationship("Reporte", back_populates="ayudante")
