import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.core.configs import settings
from src.core.database import engine
from src.models.permissao_model import PermissaoModel


async def criar_tabelas() -> None:
    print("Criando as tabelas no banco de dados.")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso.")


async def criar_permissoes() -> None:
    print("Criando as permissões no banco de dados.")
    async_session = sessionmaker(
        bind=create_async_engine(settings.DB_URL, echo=True),
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        permissao_admin = PermissaoModel(nome="admin")
        permissao_vendedor = PermissaoModel(nome="vendedor")
        permissao_cliente = PermissaoModel(nome="cliente")
        session.add(permissao_admin)
        session.add(permissao_vendedor)
        session.add(permissao_cliente)
        await session.commit()
    print("Permissões criadas com sucesso.")


async def main():
    await criar_tabelas()
    await criar_permissoes()


if __name__ == "__main__":
    asyncio.run(main())
