import yaml
from box import ConfigBox, BoxValueError
from ensure import ensure_annotations
from pathlib import Path

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