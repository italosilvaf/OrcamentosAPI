from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from models.produto_model import ProdutoModel
from models.usuario_model import UsuarioModel
from schemas.produto_schema import ProdutoSchemaBase, ProdutoSchema, ProdutoSchemaUp
from core.deps import get_session, get_current_user


router = APIRouter()


# POST Produto
@router.post('/', response_model=ProdutoSchema, status_code=status.HTTP_201_CREATED)
async def post_produto(produto: ProdutoSchemaBase, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession= Depends(get_session)):
    novo_produto: ProdutoModel = ProdutoModel(nome=produto.nome, nome_referencia=produto.nome_referencia, 
                                              codigo=produto.codigo, marca_id=produto.marca_id, categoria_id=produto.categoria_id, 
                                              unidade_de_venda=produto.unidade_de_venda, valor=produto.valor )
    
    if usuario_logado.permissao_id != 1:
        raise HTTPException(detail='O usuário logado não tem permissão para criar produtos.',
                                status_code=status.HTTP_401_UNAUTHORIZED)

    async with db as session:
        try:
            session.add(novo_produto)
            await session.commit()

            return novo_produto
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Já existe um produto cadastrado com este código.')


# GET Produtos
@router.get('/', response_model=List[ProdutoSchema], status_code=status.HTTP_200_OK)
async def get_produtos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel)
        result = await session.execute(query)
        produtos: List[ProdutoModel] = result.scalars().unique().all()
        
        if produtos:
            return produtos
        else:
            raise HTTPException(detail='Nenhum produto cadastrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# GET Produto
@router.get('/{produto_id}', response_model=ProdutoSchema, status_code=status.HTTP_200_OK)
async def get_produto(produto_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id == produto_id)
        result = await session.execute(query)
        produto: ProdutoModel = result.scalars().unique().one_or_none()

        if produto:
            return produto
        else:
            raise HTTPException(detail='Produto não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT Produto
@router.put('/{produto_id}', response_model=ProdutoSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_produto(produto_id: int, produto: ProdutoSchemaUp, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id == produto_id)
        result = await session.execute(query)
        produto_up: ProdutoModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para editar produtos.',
                                    status_code=status.HTTP_401_UNAUTHORIZED)

        if produto_up:
            if produto.nome:
                produto_up.nome = produto.nome
            if produto.nome_referencia:
                produto_up.nome_referencia = produto.nome_referencia
            if produto.codigo:
                produto_up.codigo = produto.codigo
            if produto.marca_id:
                produto_up.marca_id = produto.marca_id
            if produto.categoria_id:
                produto_up.categoria_id = produto.categoria_id
            if produto.unidade_de_venda:
                produto_up.unidade_de_venda = produto.unidade_de_venda
            if produto.valor:
                produto_up.valor = produto.valor

            try:
                await session.commit()

                return produto_up
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail='Os dados inseridos são inválidos.')
        else:
            raise HTTPException(detail='Produto não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Produto
@router.delete('/{produto_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_produto(produto_id: int, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id == produto_id)
        result = await session.execute(query)
        produto_del: ProdutoModel = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para deletar produtos.',
                                    status_code=status.HTTP_401_UNAUTHORIZED)
        
        if produto_del:
            await session.delete(produto_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Produto não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
        