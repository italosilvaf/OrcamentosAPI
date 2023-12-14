from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey,func
from sqlalchemy.orm import relationship


class ProdutoModel(settings.DBBaseModel):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(255), nullable=False)
    nome_referencia = Column(String(100), nullable=True)
    codigo = Column(String(50), unique=True, nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas.id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    unidade_de_venda = Column(String(20), nullable=False)
    valor = Column(Float, nullable=False)
    marca = relationship('MarcaModel', back_populates='produtos', lazy='joined')
    categoria = relationship('CategoriaModel', back_populates='produtos', lazy='joined')