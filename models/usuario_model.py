from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(255), nullable=True)
    telefone = Column(String(11), nullable=True)
    email = Column(String(255), index=True, nullable=True, unique=True)
    senha = Column(String(255), nullable=True)
    permissao_id = Column(Integer, ForeignKey('permissao.id'))
    