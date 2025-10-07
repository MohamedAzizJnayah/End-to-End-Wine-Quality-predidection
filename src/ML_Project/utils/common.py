import json
import yaml
from box import ConfigBox
from box.exceptions import  BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from ML_Project.logging import logger
import os


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directories(path_to_directories: list[Path] , verbose=True):
    for path in path_to_directories:
        path.mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def save_json(data:dict,file_path:Path):
    try:
        with open(file_path, "w") as f :
            json.dump(data, f, indent=4)
        logger.info(f"created json file at :{file_path}")

    except Exception as e :
        logger.error(f"Error while saving JSON file: {e}")
        raise e
    