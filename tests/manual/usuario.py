from datetime import datetime

MOCK_USUARIO_ADMIN = {
    "id": 1,
    "created_at": datetime(year=2023, month=1, day=1, hour=1, minute=1).isoformat(),
    "updated_at": datetime(year=2023, month=2, day=2, hour=2, minute=2).isoformat(),
    "cpf": "12345678909",
    "nome": "NomeTesteAdmin",
    "sobrenome": "SobrenomeTesteAdmin",
    "telefone": "34912345678",
    "email": "testeadmin@email.com",
    "permissao_id": 1,
    "senha": "290302",
}

MOCK_USUARIO_TESTE_ADMIN = {
    "id": 4,
    "created_at": datetime(year=2023, month=1, day=1, hour=1, minute=1).isoformat(),
    "updated_at": datetime(year=2023, month=2, day=2, hour=2, minute=2).isoformat(),
    "cpf": "12345678909",
    "nome": "NomeTesteAdmin",
    "sobrenome": "SobrenomeTesteAdmin",
    "telefone": "34912345678",
    "email": "testeadmin@email.com",
    "permissao_id": 1,
    "senha": "290302",
}


MOCK_USUARIO_TESTE_VENDEDOR = {
    "id": 5,
    "created_at": datetime(year=2023, month=1, day=1, hour=1, minute=1).isoformat(),
    "updated_at": datetime(year=2023, month=2, day=2, hour=2, minute=2).isoformat(),
    "cpf": "12345678909",
    "nome": "NomeTesteVendedor",
    "sobrenome": "SobrenomeTesteVendedor",
    "telefone": "34912345678",
    "email": "testevendedor@email.com",
    "permissao_id": 2,
    "senha": "290302",
}


MOCK_USUARIO_TESTE_CLIENTE = {
    "id": 6,
    "created_at": datetime(year=2023, month=1, day=1, hour=1, minute=1).isoformat(),
    "updated_at": datetime(year=2023, month=2, day=2, hour=2, minute=2).isoformat(),
    "cpf": "12345678909",
    "nome": "NomeTesteCliente",
    "sobrenome": "SobrenomeTesteCliente",
    "telefone": "34912345678",
    "email": "testecliente@email.com",
    "permissao_id": 3,
    "senha": "290302",
}
