
setup:
	poetry init
	git init
	poetry add --group dev jupyter jupyterlab ipykernel ruff radon \
					isort bandit pre-commit dvc flake8 nbconvert
	poetry run pre-commit install

install:
	poetry install

temp_install:
	python -m venv venv
	pip install -r requirements_dev.txt

data:
	dvc pull

requirements:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

requirements_dev:
	poetry export --with dev --without-hashes -f requirements.txt -o requirements_dev.txt