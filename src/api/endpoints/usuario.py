from typing import List, Optional, Any
from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchema, UsuarioSchemaUp
from core.deps import get_session, get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso


router = APIRouter()


# GET Logado
@router.get('/logado', response_model=UsuarioSchema)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


# POST Usuario / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchema)
async def post_usuario(usuario: UsuarioSchema, db: AsyncSession = Depends(get_session)):
    novo_usuario: UsuarioModel = UsuarioModel(cpf=usuario.cpf, nome=usuario.nome, sobrenome=usuario.sobrenome, telefone=usuario.telefone,
                                              email=usuario.email, senha=gerar_hash_senha(usuario.senha), permissao_id=usuario.permissao_id)
    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()

            return novo_usuario
        except IntegrityError:
            raise HTTPException(detail="Dados de usuário inválidos.",
                                status_code=status.HTTP_406_NOT_ACCEPTABLE)
        

# GET Usuarios
@router.get('/', response_model=List[UsuarioSchema])
async def get_usuarios(db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel).order_by(UsuarioModel.id)
        result = await session.execute(query)
        usuarios: List[UsuarioSchemaBase] = result.scalars().unique().all()
        
        if usuario_logado.permissao_id == 3:
            raise HTTPException(detail='O usuário logado não tem permissão para ver essas informações',
                                status_code=status.HTTP_401_UNAUTHORIZED)

        if usuarios:
            return usuarios
        else:
            raise HTTPException(detail='Nenhum usuário cadastrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# GET Usuario
@router.get('/{usuario_id}', response_model=UsuarioSchema, status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_logado.permissao_id == 3 and usuario_logado.id != usuario_id:
            raise HTTPException(detail='O usuário logado não tem permissão para ver essas informações',
                                status_code=status.HTTP_401_UNAUTHORIZED)

        if usuario:
            return usuario
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT Usuario
@router.put('/{usuario_id}', response_model=UsuarioSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int, usuario: UsuarioSchemaUp, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_logado.id != usuario_id and usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para modificar este usuário.',
                                status_code=status.HTTP_401_UNAUTHORIZED)

        if usuario_up:
            if usuario.cpf:
                usuario_up.cpf = usuario.cpf
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.sobrenome:
                usuario_up.sobrenome = usuario.sobrenome
            if usuario.telefone:
                usuario_up.telefone = usuario.telefone
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.senha:
                usuario_up.senha = gerar_hash_senha(usuario.senha)
            if usuario.permissao_id:
                if usuario_logado.permissao_id != 1:
                    raise HTTPException(detail='O usuário logado não tem permissão para modificar a permissão deste usuário.',
                                        status_code=status.HTTP_401_UNAUTHORIZED)
                usuario_up.permissao_id = usuario.permissao_id
            try:
                await session.commit()
                return usuario_up
            except IntegrityError:
                raise HTTPException(detail='Já existe um usuário com esse e-mail cadastrado',
                                status_code=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Usuario
@router.delete('/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario_id: int, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_logado.id != usuario_id and usuario_logado.permissao_id != 1:
            raise HTTPException(detail='O usuário logado não tem permissão para deletar este usuário.',
                                status_code=status.HTTP_401_UNAUTHORIZED)

        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Post Login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    usuario = await autenticar(email=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(detail='Dados de acesso incorretos.',
                            status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
