install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

check:
	selfcheck test lint

test:
	poetry run pytest