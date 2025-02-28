from app.dependencies import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, Session, joinedload
from sqlalchemy.ext.declarative import declarative_base

uri = f"{settings.DATABASE_URL}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine = create_engine(uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
