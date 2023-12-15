
run:
	poetry run python -m src.main

criar_tabelas:
	poetry run python -m src.criar_tabelas

adicionar_dados:
	poetry run python -m src.adicionar_dados

install:
	poetry env use /usr/bin/python3
	poetry lock
	poetry install