from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    id_director: Mapped[int] = mapped_column(
        Integer, ForeignKey("directores.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    director: Mapped["Director"] = relationship(
        "Director", back_populates="departamento"
    )
    materia: Mapped["Materia"] = relationship("Materia", back_populates="departamento")
