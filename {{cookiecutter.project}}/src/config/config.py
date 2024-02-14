"""
App Configuration Management Module
Overview
This module manages application configurations, utilizing dataclasses for defining configuration 
models and supporting environment-specific settings through YAML files.

Configuration Files
- Development: Uses config_dev.yaml by default.
- Production: Switches to config_prod.yaml when ENVIRONMENT is set to 'PROD'.

Environment Variables Override
Override configuration using environment variables in .env file or as exported variables.

Naming convention:
[ENV]_[CONFIG_SECTION]_[CONFIG_KEY]. For example: DEV_SECRETS_API_KEY.
[ENV]_[CONFIG_KEY]. if it doesnt have section. For example: DEV_LOG_LEVEL 
Note: Always all in caps

Usage
- Define configuration settings in the YAML files.
- Optionally override specific settings via environment variables.
- Access configurations through the Config, Secrets, and Model classes.
"""
from __future__ import annotations

import os
import pathlib
from dataclasses import dataclass
from typing import Literal

import yaml
from dacite import from_dict
from dotenv import load_dotenv


load_dotenv()

ENVIRONMENT = os.environ["ENVIRONMENT"]
config_filename = 'config_prod.yaml' if ENVIRONMENT == "PROD" else 'config_dev.yaml'


# ----------------- EXAMPLE -----------------
@dataclass
class Config:
    secrets: Secrets
    model: Model
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    environment: Literal["PROD", "DEV"]


@dataclass(repr=False)
class Secrets:
    api_key: str
    

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


def get_env_var_value(env_var_name: str,
                      environment: Literal['DEV', 'PROD'] | None=None
                      ) -> int | str | None:
    if environment:
        env_var_name = environment + '_' + env_var_name

    env_var_value = None
    if env_var_name in os.environ:
        try:
            env_var_value = int(os.environ[env_var_name])
        except ValueError:
            env_var_value = os.environ[env_var_name]
    return env_var_value

# Iterate through the keys of yaml_config to check if the corresponding env variable exists
for section_key, section_value in yaml_config.items():

    # First level
    if not isinstance(section_value, dict):
        env_var_name = f"{section_key.upper()}"
        env_var_value = get_env_var_value(env_var_name)
        if env_var_value:
            yaml_config[section_key] = env_var_value
        else:
            env_var_value = get_env_var_value(env_var_name,
                                              environment=yaml_config["environment"])
            if env_var_value:
                yaml_config[section_key] = env_var_value
        continue

    # Second Level
    for key in section_value:
        env_var_name = f"{section_key.upper()}_{key.upper()}"
        env_var_value = get_env_var_value(env_var_name)
        if env_var_value:
            yaml_config[section_key][key] = env_var_value
        else:
            env_var_value = get_env_var_value(env_var_name,
                                              environment=yaml_config["environment"])
            if env_var_value:
                yaml_config[section_key][key] = env_var_value


config: Config = from_dict(data_class=Config, data=yaml_config)
