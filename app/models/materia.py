from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Materia(Base):
    __tablename__ = "materias"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    id_departamento: Mapped[int] = mapped_column(
        Integer, ForeignKey("departamentos.id"), nullable=False
    )
    id_cordinador: Mapped[int] = mapped_column(
        Integer, ForeignKey("cordinadores.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    departamento: Mapped["Departamento"] = relationship(
        "Departamento", back_populates="materia"
    )
    materia_usuario_nota: Mapped["MateriaUsuarioNota"] = relationship(
        "MateriaUsuarioNota", back_populates="materia"
    )
    cordinador: Mapped["Cordinador"] = relationship(
        "Cordinador", back_populates="materia"
    )
    seccion: Mapped["Seccion"] = relationship("Seccion", back_populates="materia")
