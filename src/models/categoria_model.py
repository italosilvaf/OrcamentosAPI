from src.core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from src.models.produto_model import ProdutoModel


class CategoriaModel(settings.DBBaseModel):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(50), nullable=False)
    produtos = relationship("ProdutoModel", back_populates='categoria', lazy='joined')
