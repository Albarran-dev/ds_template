<!-- ![Python Version](https://img.shields.io/badge/python-3.8-blue) -->
![Maintainer](https://img.shields.io/badge/owner-{{cookiecutter.owner}}-green)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
# {{cookiecutter.project}}
-----------------------------
# Checklist
- [ ] Leer Oferta del proyecto
- [ ] Añadir el remote del devops a git
- [ ] Revisar scope con {{cookiecutter.owner}} y PM
- [ ] Revisar Diseño y Arquitectura con {{cookiecutter.owner}} y PM
- [ ] En el caso de usar dvc, crear un blob_storage y añadir el connection_string al .env
# Introduction

# Getting Started
### Requirements
#### Docker
Docker must be installed.
#### Make
For all the referenced `make` commands, it has to be installed, for unix systems
its installed by defaults, in windows you can use winget(`winget install GnuWin32.Make`) or choco(`choco install make`) for example.
If you dont want to install `make` you can look up the corresponding commands on the `Makefile`.


### Using poetry
Be sure to have poetry and the required python version running.
For creating the environment and installing the dependencies
run `make install`.
Be sure to activate the virtual environment, vscode will promp you to use the detected venv,
just open a new terminal window, it should be activated.
For manual activation run `poetry shell`.
### Using venv
If you preffer using venv, use `make venv_install` to create a virtual environment
using the requirements_dev.txt.
### Using devcontainers
Create the container using `make amd_container` or `make arm_container` if you are using a arm architecture.
When the image is build you can run the container with `make run_amd_container` or `make run_arm_container` respectively.
Alternatively you can download already generated images with `make data`.

## DVC
For using dvc you first have to set it up: `make dvc_setup`

For more information on dvc data-management : [https://dvc.org/doc/start/data-management/data-versioning](dvc-data-versioning)
After dvc is setup just run `make data`  to download the dvc tracked data.

## Credentials
* The `.env` has all the necesary credentials related to the following services:
    * DVC
    * .env encryption key

For decrypting the `.env.enc` you need at least the openssl key on you .env.
You can update/rewrite your .env decrypting this file with `make decrypt_env`

# Deployment
For deploying the container, it can be automatically created and uploaded to the ACI(if the appropiate credentials are on the .env) with `make push_amd_container`.  
If you just want to create the image: `make amd_container`.  
In case an arm architecture is needed: `make arm_container`.  

## Runs
How to run ?


# Data
Data used

# Next Steps

# Other Resources

Made by the turing data science team.