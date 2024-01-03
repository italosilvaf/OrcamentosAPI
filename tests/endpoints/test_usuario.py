import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_201_CREATED,
)


@pytest.mark.parametrize(
    ("cpf", "nome", "sobrenome", "telefone", "email", "permissao_id", "senha"),
    [
        (
            "12345678909",
            "NomeTesteAdmin",
            "SobrenomeTesteAdmin",
            "34912345678",
            "testeadmin@email.com",
            1,
            "290302",
        ),
        (
            "12345678910",
            "NomeTesteVendedor",
            "SobrenomeTesteVendedor",
            "34912345678",
            "testevendedor@email.com",
            2,
            "290302",
        ),
        (
            "12345678911",
            "NomeTesteCliente",
            "SobrenomeTesteCliente",
            "34912345678",
            "testecliente@email.com",
            3,
            "290302",
        ),
    ],
)
@pytest.mark.asyncio()
@pytest.mark.usefixtures("create_database")
async def test_signup_usuario_sucesso(
    cpf,
    nome,
    sobrenome,
    telefone,
    email,
    permissao_id,
    senha,
    async_client: AsyncClient,
):
    payload = {
        "cpf": cpf,
        "nome": nome,
        "sobrenome": sobrenome,
        "telefone": telefone,
        "email": email,
        "permissao_id": permissao_id,
        "senha": senha,
    }

    response = await async_client.post("/usuarios/signup", json=payload)
    data = response.json()

    assert response.status_code == HTTP_201_CREATED
    assert data["cpf"] == cpf
    assert data["nome"] == nome
    assert data["sobrenome"] == sobrenome
    assert data["telefone"] == telefone
    assert data["email"] == email
    assert data["permissao_id"] == permissao_id
