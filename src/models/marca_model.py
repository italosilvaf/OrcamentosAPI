from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from src.core.configs import settings


class MarcaModel(settings.DBBaseModel):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    nome = Column(String(50), nullable=False)
    produtos = relationship("ProdutoModel", back_populates="marca", lazy="joined")
