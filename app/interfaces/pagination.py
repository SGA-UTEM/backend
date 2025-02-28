from pydantic import BaseModel
from typing import Optional


class Params(BaseModel):
    Limit: int
    Page: int
