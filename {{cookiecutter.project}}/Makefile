include .env
.PHONY: data

TIMESTAMP := $(shell date +%Y%m%d%H%M%S)
COMMIT_HASH := $(shell git rev-parse --short HEAD)

# Architecture: amd or arm
ARCH = amd

# Azure
RESOURCE_GROUP = ??
## Container Registry Info
CONTAINER_REGISTRY_URL=??
CONTAINER_REGISTRY_USERNAME=??
## ACI
CONTAINER_INSTANCE_NAME=??


setup: _sure_to_continue_setup
	git init
	poetry add --group dev jupyter jupyterlab ipykernel ruff radon \
					isort bandit pre-commit dvc flake8 nbconvert pytest
	poetry add dacite pyyaml python-dotenv
	poetry run pre-commit install
	# pre-commit install -t pre-push
	poetry self add poetry-plugin-export
	make _create-dotenv
	make requirements
	make requirements_dev

dvc_setup:
	dvc remote modify --local $(DVC_REMOTE) connection_string $(DVC_REMOTE_CONN_STR)

encrypt_env:
	openssl enc -aes-256-cbc -salt -pbkdf2 -in .env -out .env.enc -pass pass:$(OPENSSL_KEY)

decrypt_env: _sure_to_continue_decryption
	openssl enc -aes-256-cbc -d -salt -pbkdf2 -in .env.enc -out .env -pass pass:$(OPENSSL_KEY)

install:
	poetry install

venv_install:
	python -m venv venv
	pip install -r requirements_dev.txt

data:
	dvc pull

requirements:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

requirements_dev:
	poetry export --with dev --without-hashes -f requirements.txt -o requirements_dev.txt

container:
	docker buildx build --platform linux/$(ARCH)64 -t {{cookiecutter.project}}_$(ARCH) .

dev_container:
	docker buildx build --platform linux/$(ARCH)64 --target dev -t {{cookiecutter.project}}_$(ARCH) .

push_container: container
	docker login $(CONTAINER_REGISTRY_URL) --username $(CONTAINER_REGISTRY_USERNAME) --password $(ACR_PWD)
	docker tag {{cookiecutter.project}}_$(ARCH):latest \
			    $(CONTAINER_REGISTRY_URL)/{{cookiecutter.project}}_$(ARCH):$(COMMIT_HASH)
	docker push $(CONTAINER_REGISTRY_URL)/{{cookiecutter.project}}_$(ARCH):$(COMMIT_HASH)

# Deploy an Azure container instance
deploy_container_dev: push_container delete_container_dev
	az container create \
		--resource-group $(RESOURCE_GROUP) \
		--name CONTAINER_INSTANCE_NAME \
		--registry-login-server $(CONTAINER_REGISTRY_URL) \
		--registry-username $(CONTAINER_REGISTRY_USERNAME) \
		--registry-password $(ACR_PWD) \
		--image $(CONTAINER_REGISTRY_URL)/mscorp_pws_drafter_amd:$(COMMIT_HASH) \
		--dns-name-label CONTAINER_INSTANCE_NAME \
		--ports 8000 \
		--secure-environment-variables \
			# SECRETS_API_KEY=$(DEV_SECRETS_API_KEY) \
		--environment-variables \
			# PARAMS_SPLIT_CHUNKSIZE_CHARS=5000 \
			ENVIRONMENT="DEV" \
		--cpu 4 \
		--memory 8 \
		--protocol TCP

delete_container_dev:
	az container delete \
		--resource-group $(RESOURCE_GROUP) \
		--name CONTAINER_INSTANCE_NAME \
		--yes
# -----------------------------------

_create-dotenv:
	echo OPENSSL_KEY=\"$$(openssl rand -base64 32)\" > .env
	echo DVC_REMOTE_CONN_STR=\"\" >> .env
	echo DVC_REMOTE=\"\" >> .env
	echo ENVIRONMENT=\"DEV\" >> .env

_sure_to_continue_setup:
	@read -p "Ensure that the correct python version({{cookiecutter.python_version}}) is already setup, continue? [Y/n]: " answer; \
	if [ "$$answer" != "n" ] && [ "$$answer" != "N" ]; then \
		echo "Continuing with setup..."; \
	else \
		echo "Setup aborted."; \
		exit 1; \
	fi

_sure_to_continue_decryption:
	@read -p "The current .env file will be overwritten, Are you sure you want to continue? [Y/n]: " answer; \
	if [ "$$answer" != "n" ] && [ "$$answer" != "N" ]; then \
		echo "Continuing with decryption..."; \
	else \
		echo "Decryption aborted."; \
		exit 1; \
	fi