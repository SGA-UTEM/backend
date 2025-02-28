from sqlalchemy import *
from sqlalchemy.orm import *
from app.db.db import Base
from app.models import *
import datetime

now = datetime.timezone.utc


class FechaPostulacion(Base):
    __tablename__ = "fechas_postulaciones"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    inicio: Mapped[Date] = mapped_column(DateTime, unique=True, nullable=False)
    fin: Mapped[Date] = mapped_column(DateTime, nullable=False)
    is_asigned: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[Date] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
