
from __future__ import annotations
from typing import Optional, Literal
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

config: Config = from_dict(data_class=Config, data=yaml_config)
