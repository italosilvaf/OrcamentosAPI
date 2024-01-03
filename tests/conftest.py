from collections.abc import AsyncGenerator, Generator

import pytest
import asyncio
import pytest_asyncio
from httpx import AsyncClient
from src.core.database import engine
from src.core.configs import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.models.permissao_model import PermissaoModel

from src.main import app


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def async_client() -> AsyncGenerator:
    async_client_instance = AsyncClient(
        app=app,
        base_url="http://0.0.0.0:8000/api",
    )
    async with async_client_instance:
        yield async_client_instance


@pytest_asyncio.fixture(scope="function")
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

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
