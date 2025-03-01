from pydantic import BaseModel


class Evaluation(BaseModel):
    value: int
    content: str
    id_section: int
    id_helper: int
