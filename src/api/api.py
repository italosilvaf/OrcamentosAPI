from fastapi import APIRouter

from src.api.endpoints import categoria, marca, produto, usuario

api_router = APIRouter()

api_router.include_router(produto.router, prefix="/produtos", tags=["produtos"])
api_router.include_router(categoria.router, prefix="/categorias", tags=["categorias"])
api_router.include_router(marca.router, prefix="/marcas", tags=["marcas"])
api_router.include_router(usuario.router, prefix="/usuarios", tags=["usuarios"])
