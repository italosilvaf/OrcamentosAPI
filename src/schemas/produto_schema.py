from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProdutoSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    nome_referencia: Optional[str]
    codigo: str
    marca_id: int
    categoria_id: int
    unidade_de_venda: str
    valor: float

    class Config:
        orm_mode = True


class ProdutoSchema(ProdutoSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProdutoSchemaUp(ProdutoSchemaBase):
    nome: Optional[str]
    nome_referencia: Optional[str]
    codigo: Optional[str]
    marca_id: Optional[int]
    categoria_id: Optional[int]
    unidade_de_venda: Optional[str]
    valor: Optional[float]