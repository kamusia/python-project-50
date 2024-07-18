install:
	poetry install

build:
	poetry build

check:
	make lint
	make test

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
   
