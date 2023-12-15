from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from src.core.configs import settings


class PermissaoModel(settings.DBBaseModel):
    __tablename__ = "permissoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(20), unique=True, nullable=False)
    usuarios = relationship("UsuarioModel", back_populates="permissao", lazy="joined")
