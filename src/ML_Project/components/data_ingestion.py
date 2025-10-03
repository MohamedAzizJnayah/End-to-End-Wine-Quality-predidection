
import urllib.request as request
import zipfile 
from ML_Project.entity.config_entity import DataIngestionConfig
from  ML_Project.logging import logger
from ML_Project.utils.common import get_size
from pathlib import Path
from urllib import request
import zipfile
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Download file
    def download_file(self):
        local_file = Path(self.config.local_data_file)
        local_file.parent.mkdir(parents=True, exist_ok=True)
        if not local_file.exists():
            filename, headers = request.urlretrieve(
                self.config.source_url,
                local_file
            )
            logger.info(f"File downloaded successfully! Size: {get_size(Path(filename))}")
        else:
            logger.info(f"File already exists of size: {get_size(local_file)}")
        return local_file

    # Extracting zip file
    def extract_zip_file(self):
        unzip_dir = Path(self.config.unzip_dir)
        unzip_dir.mkdir(parents=True, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
        logger.info(f"File extracted successfully in dir: {unzip_dir}")

        # Parcourir tous les fichiers extraits
        for file_path in unzip_dir.iterdir():
            if file_path.is_file():  # seulement les fichiers
                try:
                    # Essayer de lire avec pandas
                    df = pd.read_csv(file_path)
                    logger.info(f"Displaying first 5 rows of {file_path.name}:\n{df.info()}")
                except Exception as e:
                    logger.warning(f"Cannot read {file_path.name} with pandas: {e}")
        
        return unzip_dir
