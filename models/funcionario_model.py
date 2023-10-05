from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship


class FuncionarioModel(settings.DBBaseModel):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    cpf = Column(String(11), unique=True)
    nome = Column(String(100))
    sobrenome = Column(String(255), nullable=True)
    telefone = Column(String(11), nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("UsuarioModel", back_populates='funcionarios', lazy='joined')
