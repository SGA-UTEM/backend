from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class Evaluation(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    id_section: Mapped[int] = mapped_column(
        Integer, ForeignKey("secciones.id"), nullable=False
    )
    id_helper: Mapped[int] = mapped_column(
        Integer, ForeignKey("ayudantes.id"), nullable=False
    )
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )

    ayudante: Mapped["Ayudante"] = relationship("Ayudante", back_populates="evaluation")
    seccion: Mapped["Seccion"] = relationship("Seccion", back_populates="evaluation")
