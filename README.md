<h1 align="center">
    <img alt="cookiecutter Logo" width="200px" src="https://raw.githubusercontent.com/cookiecutter/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png">
</h1>

<div align="center">  
</div>

# DS_Template
This is a template for developing data science projects.  

# Requirements
* Cookiecutter: [cookiecutter-installation](https://cookiecutter.readthedocs.io/en/stable/installation.html)
* Poetry: [poetry-installation](https://python-poetry.org/docs/#installation)  
* Makefile (Run `winget install GnuWin32.Make`)
* Pyenv(optional)
# Usage
To use the template:  

0. Install Requirements  
1. Run on the terminal:  
   > cookiecutter https://github.com/Albarran-dev/ds_template/

2. Fill the required fields(eg: project, owner)
3. Set up the appropiate version of python, pyenv example:\
    > pyenv local 3.9.16  

   If the version of python wasnt installed run this first
   > pyenv install 3.9.16  
4. Run on the terminal:  
   > make setup  

   This will initialize poetry, git, install some basic dependencies and install pre-commit



# Resources
* Want to know more about poetry?, check out [Poetry: The Game-Changer in Python Dependency Management](https://python.plainenglish.io/poetry-the-game-changer-in-python-dependency-management-49c4861e5801)  
   

# Structure

├── .devcontainer       - Container Configuration  
├── .dvc                - DVC configuration  
├── .vscode             - VSCode Configuration  
├── artifacts           - All outputs generated (except models): files, video, images...  
├── containers          - Docker containers used  
├── data                - Data to use as input on the project  
├── docs                - Documentation files  
├── models              - Trained and serialized models, model predictions, or model summaries  
├── notebooks           - Jupyter notebooks  
├── references          - Data dictionaries, manuals, papers, and all other explanatory materials  
├── reports             - Generated analysis as HTML, PDF, LaTeX, etc.  
│   └── figures         - Generated graphics and figures to be used in reporting  
├── runners             - Executable scripts  
├── src                 - Source code for use in this project  
│   ├── __init__.py     - Makes src a Python module  
│   ├── config          - Configuration of the project  
│   │   ├── config.py   - Set Dataclass structure of the configuration  
│   │   └── config.yaml - YAML file with all the configuration  
│   ├── models          - Scripts to train models and then use trained models to make predictions  
│   │   ├── predict_model.py  
│   │   └── train_model.py  
│   ├── azure           - Azure pipelines, functions, etc.  
│   └── ...             - Rest of the code  
├── tests               - Testing  
├── .env                - For storing sensible credentials  
├── .gitignore          - gitignore  
├── .pre-commit-config.yml - pre-commit hooks configuration  
├── Dockerfile          - Template for making a Multistage Dockerfile  
├── Makefile            - Makefile with commands like `make setup` or `make install`  
├── poetry.lock         - Poetry lock that ensures environment reproducibility  
├── poetry.toml         - Poetry configuration  
├── pyproject.toml      - Poetry requirements specification file and other configurations  
├── README.md           - The top-level README for developers using this project  
└── requirements.txt    - The requirements file for reproducing the production environment, e.g., generated with `make requirements`
└── requirements_dev.txt    - The requirements file for reproducing the development environment, e.g., generated with `make requirements_dev`
