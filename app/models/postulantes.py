from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Postulante(Base):
    __tablename__ = "postulantes"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    prioridad: Mapped[int] = mapped_column(Integer, nullable=False)
    id_materia_usuario_nota: Mapped[int] = mapped_column(
        Integer, ForeignKey("materias_usuario_notas.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    materia_usuario_nota: Mapped["MateriaUsuarioNota"] = relationship(
        "MateriaUsuarioNota", back_populates="postulante"
    )
