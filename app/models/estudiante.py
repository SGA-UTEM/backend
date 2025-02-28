from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    rut: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    estudiante_regular: Mapped[bool] = mapped_column(Boolean, nullable=True)
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
    ayudante: Mapped["Ayudante"] = relationship("Ayudante", back_populates="estudiante")
    materia_usuario_nota: Mapped["MateriaUsuarioNota"] = relationship(
        "MateriaUsuarioNota", back_populates="estudiante"
    )
