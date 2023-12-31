from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.deps import get_current_user, get_session
from src.models.marca_model import MarcaModel
from src.models.usuario_model import UsuarioModel
from src.schemas.marca_schema import MarcaSchema, MarcaSchemaBase, MarcaSchemaUp

router = APIRouter()


# POST Marca
@router.post("/", response_model=MarcaSchema, status_code=status.HTTP_201_CREATED)
async def post_marca(
    marca: MarcaSchemaBase,
    usuario_logado: UsuarioModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    nova_marca: MarcaModel = MarcaModel(nome=marca.nome)

    if usuario_logado.permissao_id != 1:
        raise HTTPException(
            detail="O usuário logado não tem permissão para criar marcas.",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    db.add(nova_marca)
    await db.commit()

    return nova_marca


# GET Marcas
@router.get("/", response_model=List[MarcaSchema], status_code=status.HTTP_200_OK)
async def get_produtos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel).order_by(MarcaModel.id)
        result = await session.execute(query)
        marcas: List[MarcaModel] = result.scalars().unique().all()

        if marcas:
            return marcas
        else:
            raise HTTPException(
                detail="Nenhuma marca cadastrada.",
                status_code=status.HTTP_404_NOT_FOUND,
            )


# GET Marca
@router.get("/{marca_id}", response_model=MarcaSchema, status_code=status.HTTP_200_OK)
async def get_marca(marca_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca: MarcaModel = result.scalars().unique().one_or_none()

        if marca:
            return marca
        else:
            raise HTTPException(
                detail="Marca não encontrada.", status_code=status.HTTP_404_NOT_FOUND
            )


# PUT Marca
@router.put(
    "/{marca_id}", response_model=MarcaSchemaBase, status_code=status.HTTP_202_ACCEPTED
)
async def put_marca(
    marca_id: int,
    marca: MarcaSchemaUp,
    usuario_logado: UsuarioModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca_up: MarcaModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(
                detail="O usuário logado não tem permissão para editar marcas.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if marca_up:
            if marca.nome:
                marca_up.nome = marca.nome

            await session.commit()

            return marca_up
        else:
            raise HTTPException(
                detail="Marca não encontrada.", status_code=status.HTTP_404_NOT_FOUND
            )


# DELETE Marca
@router.delete("/{marca_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_produto(
    marca_id: int,
    usuario_logado: UsuarioModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == marca_id)
        result = await session.execute(query)
        marca_del: MarcaModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(
                detail="O usuário logado não tem permissão para deletar marcas.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if marca_del:
            await session.delete(marca_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail="Marca não encontrada.", status_code=status.HTTP_404_NOT_FOUND
            )
