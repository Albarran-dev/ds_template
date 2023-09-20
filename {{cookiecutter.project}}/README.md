# {{cookiecutter.project}}
-----------------------------
# Introduction


# Set-Up
Be sure to have poetry and the required python version running(pyenv can help with this).
For creating the environment and installing the dependencies
run `make install`.
Be sure to activate the virtual environment, vscode will promp you to use the detected venv,
just open a new terminal window, it should be activated.
For manual activation run `poetry shell`.
As a temporal fix, use `make temp_install` to create a virtual environment
using the requirements_dev.txt.
For using dvc the remote and connection_string must be added
for dvc:
> dvc remote add -d blob_origin azure://mycontainer/path

Add blob connection string:
> dvc remote modify --local blob_origin connection_string 'mysecret'

For more information on dvc data-management : [https://dvc.org/doc/start/data-management/data-versioning](dvc-data-versioning)
After dvc is setup just run `make data`  to download the dvc tracked data.

## Credentials
* The dvc connection_string for accesing the dvc tracked files.
* `.env` file ??


## Runs
How to run ?


# Data
Data used

# Next Steps

# Other Resources

Made by the turing data science team.