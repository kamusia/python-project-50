install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

check:
	make lint
	make test

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
   
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

setup: build publish package-install