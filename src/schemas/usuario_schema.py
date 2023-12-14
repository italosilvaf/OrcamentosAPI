from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    cpf: str
    nome: str
    sobrenome: str
    telefone: str
    email: EmailStr
    permissao_id: int

    class Config:
        orm_mode = True


class UsuarioSchema(UsuarioSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    senha: str


class UsuarioSchemaUp(UsuarioSchemaBase):
    cpf: Optional[str]
    nome: Optional[str]
    sobrenome: Optional[str]
    telefone: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    permissao_id: Optional[int]
    