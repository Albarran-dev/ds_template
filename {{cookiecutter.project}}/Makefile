
setup: _sure_to_continue
	poetry init
	git init
	poetry add --group dev jupyter jupyterlab ipykernel ruff radon \
					isort bandit pre-commit dvc flake8 nbconvert
	make _add_configuration
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

_add_configuration:
	@echo "[tool.ruff]" >> pyproject.toml
	@echo "line-length = 100" >> pyproject.toml
	@echo "select = [\"E\", \"F\", \"N\", \"B\", \"ARG\", \"PL\", \"ERA\", \"SIM\", \"RUF\"]" >> pyproject.toml
	@echo "ignore = [\"B905\", \"E402\"]" >> pyproject.toml
	@echo "" >> pyproject.toml
	@echo "[tool.flake8]" >> pyproject.toml
	@echo "select = \"C901\"" >> pyproject.toml
	@echo "max-line-length = 100" >> pyproject.toml
	@echo "" >> pyproject.toml
	@echo "[tool.isort]" >> pyproject.toml
	@echo "multi_line_output = 0" >> pyproject.toml
	@echo "combine_as_imports = true" >> pyproject.toml
	@echo "lines_after_imports = 2" >> pyproject.toml
	@echo "remove_redundant_aliases = false" >> pyproject.toml
	@echo "indent = \"    \"" >> pyproject.toml

_sure_to_continue:
	@read -p "Ensure the correct python version is already setup, continue? [Y/n]: " answer; \
	if [ "$$answer" != "n" ] && [ "$$answer" != "N" ]; then \
		echo "Continuing with setup..."; \
	else \
		echo "Setup aborted."; \
		exit 1; \
	fi