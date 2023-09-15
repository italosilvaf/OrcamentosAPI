from sqlalchemy import Integer, String, Column, Boolean
from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=True)
    telefone = Column(String(11), nullable=True)
    email = Column(String(255), index=True, nullable=True, unique=True)
    senha = Column(String(255), nullable=True)
    eh_admin = Column(Boolean, default=False)
    