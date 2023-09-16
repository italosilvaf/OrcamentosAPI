from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, func


class PermissaoModel(settings.DBBaseModel):
    __tablename__ = 'permissao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(20), unique=True, nullable=True)
    