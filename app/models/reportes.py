from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Reporte(Base):
    __tablename__ = "reportes"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    contenido: Mapped[str] = mapped_column(String, nullable=False)
    id_ayudante: Mapped[int] = mapped_column(
        Integer, ForeignKey("ayudantes.id"), nullable=False
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
    ayudante: Mapped["Ayudante"] = relationship("Ayudante", back_populates="reporte")
    seccion: Mapped["Seccion"] = relationship("Seccion", back_populates="reporte")
