from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class FuncionarioSchemaBase(BaseModel):
    id: Optional[int] = None
    cpf: str
    nome: str
    sobrenome: Optional[str]
    telefone: Optional[str]
    usuario_id: Optional[int]

    class Config:
        orm_mode = True


class FuncionarioSchema(FuncionarioSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class FuncionarioSchemaUp(FuncionarioSchemaBase):
    cpf: Optional[str]
    nome: Optional[str]
    sobrenome: Optional[str]
    telefone: Optional[str]
    usuario_id: Optional[int]
    