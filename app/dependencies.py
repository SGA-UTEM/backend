# Fastapi
import fastapi
import fastapi.openapi.utils as openapi
import fastapi.responses as responses

status = fastapi.status
# Typing
import typing

# Pydantic
import pydantic

import pydantic.generics as generics

# Starlette
import starlette.exceptions as exceptions
from starlette_context import context, plugins
from starlette_context.middleware import RawContextMiddleware

# CORS
import fastapi.middleware.cors as cors

# Interfaces
from app.interfaces.res import Res

# Settings
from app.core.settings import settings

# Config
from app.core.config import configuration

# Security
import fastapi.security as security

# Utils

# DB
from app.db.db import uri

# SQLAlchemy for PostgreSQL
from sqlalchemy import create_engine

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
