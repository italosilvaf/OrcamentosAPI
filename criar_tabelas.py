from core.configs import settings
from core.database import engine
from models.permissao_model import PermissaoModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


async def criar_tabelas() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados.')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso.')


async def criar_permissoes() -> None:
    print('Criando as permissões no banco de dados.')
    async_session = sessionmaker(
        bind=create_async_engine(settings.DB_URL, echo=True), 
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with async_session() as session:
        permissao_admin = PermissaoModel(nome='admin')
        permissao_vendedor = PermissaoModel(nome='vendedor')
        permissao_cliente = PermissaoModel(nome='cliente')
        session.add(permissao_admin)
        session.add(permissao_vendedor)
        session.add(permissao_cliente)
        await session.commit()
    print('Permissões criadas com sucesso.')


if __name__ == '__main__':
    import asyncio

    asyncio.run(criar_tabelas())
    asyncio.run(criar_permissoes())