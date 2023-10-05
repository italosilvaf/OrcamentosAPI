from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship
from models.permissao_model import PermissaoModel
from models.funcionario_model import FuncionarioModel


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    email = Column(String(255), unique=True)
    senha = Column(String(255))
    permissao_id = Column(Integer, ForeignKey('permissoes.id'))
    permissao = relationship('PermissaoModel', back_populates='usuarios', lazy='joined')
    funcionarios = relationship("FuncionarioModel", back_populates='usuario', lazy='joined')
