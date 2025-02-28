from app.dependencies import typing
from app.dependencies import generics
from app.dependencies import pydantic

T = typing.TypeVar("T", bound=pydantic.BaseModel)


class Res(pydantic.BaseModel, typing.Generic[T]):
    success: bool
    body: typing.Optional[T]
    message: typing.Optional[str] = pydantic.Field(example="error message")
