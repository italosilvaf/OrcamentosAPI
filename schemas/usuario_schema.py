from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    permissao_id: Optional[int] 

    class Config:
        orm_mode = True


class UsuarioSchema(UsuarioSchemaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    senha: str


class UsuarioSchemaUp(UsuarioSchemaBase):
    email: Optional[EmailStr]
    senha: Optional[str]
    permissao_id: Optional[int]
    