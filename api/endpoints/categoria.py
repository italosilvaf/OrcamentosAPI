from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from models.categoria_model import CategoriaModel
from models.usuario_model import UsuarioModel
from schemas.categoria_schema import CategoriaSchemaBase, CategoriaSchema, CategoriaSchemaUp
from core.deps import get_session, get_current_user


router = APIRouter()


# POST Categoria
@router.post('/', response_model=CategoriaSchema, status_code=status.HTTP_201_CREATED)
async def post_categoria(categoria: CategoriaSchemaBase, usuario_logado: UsuarioModel = Depends(get_current_user),
                         db: AsyncSession= Depends(get_session)):
    nova_categoria = CategoriaModel(nome=categoria.nome)

    if usuario_logado.permissao_id != 1:
        raise HTTPException(detail='O usuário logado não tem permissão para criar categorias.',
                                status_code=status.HTTP_401_UNAUTHORIZED)

    async with db as session:
        try:
            session.add(nova_categoria)
            await session.commit()

            return nova_categoria
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Os dados inseridos são inválidos.')


# GET Categorias
@router.get('/', response_model=List[CategoriaSchema])
async def get_produtos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel)
        result = await session.execute(query)
        categorias: List[CategoriaModel] = result.scalars().unique().all()

        if categorias:
            return categorias
        else:
            raise HTTPException(detail='Nenhuma categoria cadastrada.',
                                status_code=status.HTTP_404_NOT_FOUND)

# GET Categoria
@router.get('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_200_OK)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria: CategoriaModel = result.scalars().unique().one_or_none()

        if categoria:
            return categoria
        else:
            raise HTTPException(detail='Categoria não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)
        
# PUT Categoria
@router.put('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_categoria(categoria_id: int, categoria: CategoriaSchemaUp, usuario_logado: UsuarioModel = Depends(get_current_user),
                        db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_up: CategoriaModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para editar categorias.',
                                    status_code=status.HTTP_401_UNAUTHORIZED)
        if categoria_up:
            if categoria.nome:
                categoria_up.nome = categoria.nome

            await session.commit()

            return categoria_up
        else:
            raise HTTPException(detail='Categoria não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Categoria
@router.delete('/{categoria_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_produto(categoria_id: int, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_del: CategoriaModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para deletar categorias.',
                                    status_code=status.HTTP_401_UNAUTHORIZED)

        if categoria_del:
            await session.delete(categoria_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Categoria não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)
        