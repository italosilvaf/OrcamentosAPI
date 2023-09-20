from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey,func
from sqlalchemy.orm import relationship
from models.marca_model import MarcaModel
from models.categoria_model import CategoriaModel


class ProdutoModel(settings.DBBaseModel):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(255))
    nome_referencia = Column(String(100))
    codigo = Column(String(50), unique=True, nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas.id'))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    unidade_de_venda = Column(String(20))
    valor = Column(Float)
    marca = relationship('MarcaModel', back_populates='produtos', lazy='joined')
    categoria = relationship('CategoriaModel', back_populates='produtos', lazy='joined')