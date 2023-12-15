from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MarcaSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True


class MarcaSchema(MarcaSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class MarcaSchemaUp(MarcaSchemaBase):
    nome: Optional[str]
