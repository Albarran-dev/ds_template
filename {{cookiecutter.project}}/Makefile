
setup: _sure_to_continue
	git init
	poetry add --group dev jupyter jupyterlab ipykernel ruff radon \
					isort bandit pre-commit dvc flake8 nbconvert pytest
	poetry add dacite pyyaml python-dotenv
	poetry run pre-commit install
	make requirements
	make requirements_dev

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

container:
	docker buildx build --platform linux/amd64 -t {{cookiecutter.project}}_amd .

dev_container:
	docker buildx build --platform linux/amd64 --target dev -t {{cookiecutter.project}}_amd .

mac_container:
	docker buildx build --platform linux/arm64 -t {{cookiecutter.project}}_arm .

mac_dev_container:
	docker buildx build --platform linux/arm64 --target dev -t {{cookiecutter.project}}_arm .

_sure_to_continue:
	@read -p "Ensure that the correct python version({{cookiecutter.python_version}}) is already setup, continue? [Y/n]: " answer; \
	if [ "$$answer" != "n" ] && [ "$$answer" != "N" ]; then \
		echo "Continuing with setup..."; \
	else \
		echo "Setup aborted."; \
		exit 1; \
	fi