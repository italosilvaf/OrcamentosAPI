from src.core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.models.permissao_model import PermissaoModel


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    cpf = Column(String(11), nullable=False)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    telefone = Column(String(11), nullable=False)
    email = Column(String(255), index=True, nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    permissao_id = Column(Integer, ForeignKey('permissoes.id'), nullable=False)
    permissao = relationship('PermissaoModel', back_populates='usuarios', lazy='joined')