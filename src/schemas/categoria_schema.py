from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoriaSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True


class CategoriaSchema(CategoriaSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CategoriaSchemaUp(CategoriaSchemaBase):
    nome: Optional[str]
