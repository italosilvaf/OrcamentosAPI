from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.marca_model import MarcaModel
from schemas.marca_schema import MarcaSchemaBase, MarcaSchema, MarcaSchemaUp
from core.deps import get_session


router = APIRouter()


# POST Marca
@router.post('/', response_model=MarcaSchemaBase, status_code=status.HTTP_201_CREATED)
async def post_marca(marca: MarcaSchema, db: AsyncSession= Depends(get_session)):
    nova_marca: MarcaModel = MarcaModel(nome=marca.nome)

    db.add(nova_marca)
    await db.commit()

    return nova_marca


# GET Marcas
@router.get('/', response_model=List[MarcaSchema], status_code=status.HTTP_200_OK)
async def get_produtos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel)
        result = await session.execute(query)
        marcas: List[MarcaModel] = result.scalars().unique().all()

        if marcas:
            return marcas
        else:
            raise HTTPException(detail='Nenhuma marca cadastrada.',
                                status_code=status.HTTP_404_NOT_FOUND)


# GET Marca
@router.get('/{marca_id}', response_model=MarcaSchema, status_code=status.HTTP_200_OK)
async def get_marca(marca_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca: MarcaModel = result.scalars().unique().one_or_none()

        if marca:
            return marca
        else:
            raise HTTPException(detail='Marca não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)
        
# PUT Marca
@router.put('/{marca_id}', response_model=MarcaSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_marca(marca_id: int, marca: MarcaSchemaUp, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca_up: MarcaModel = result.scalars().unique().one_or_none()

        if marca_up:
            if marca.nome:
                marca_up.nome = marca.nome

            await session.commit()

            return marca_up
        else:
            raise HTTPException(detail='Marca não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Marca
@router.delete('/{marca_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_produto(marca_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca_del: MarcaModel = result.scalars().unique().one_or_none()

        if marca_del:
            await session.delete(marca_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Marca não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)
        