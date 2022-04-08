from pydantic import BaseModel, Field


class Vivienda(BaseModel):
    tipo: str
    ciudad: str
    titulo: str | None
    precio: int | None = Field(gt=0)
