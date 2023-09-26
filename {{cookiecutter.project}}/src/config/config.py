
from __future__ import annotations
import os
import pathlib
from dataclasses import dataclass

import yaml
from dacite import from_dict


# ----------------- EXAMPLE -----------------
@dataclass
class Config:
    files: Files
    model: Model


@dataclass
class Files:
    train_data: str
    test_data: str
    

@dataclass
class Model:
    epochs: int
    lr: float
    L1: float
    
# -------------------------------------------
config_dir = pathlib.Path(__file__).parent
CONFIG_PATH = pathlib.PurePath(config_dir, 'config.yaml')
with open(CONFIG_PATH, 'r') as file:
    yaml_config = yaml.safe_load(file)


# Iterate through the keys of yaml_config to check if the corresponding env variable exists
for section_key, section_value in yaml_config.items():
    for key in section_value:
        env_var_name = f"{section_key.upper()}_{key.upper()}"
        if env_var_name in os.environ:
            # TODO: Improve type casting from env variables
            try:
                env_var_value = int(os.environ[env_var_name])
            except ValueError:
                env_var_value = os.environ[env_var_name]

            yaml_config[section_key][key] = env_var_value

# Write the modified dictionary back to the config.yaml file
with open(CONFIG_PATH, 'w') as file:
    yaml.dump(yaml_config, file)

config: Config = from_dict(data_class=Config, data=yaml_config)
