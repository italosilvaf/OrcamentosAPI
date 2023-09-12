from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class CategoriaModel(settings.DBBaseModel):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(50))
