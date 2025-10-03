
from ML_Project.constants import *
from ML_Project.entity.config_entity import DataIngestionConfig
from ML_Project.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath= SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([Path(self.config.artifact_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
    
        config = self.config.data_ingestion
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            artifact_dir=self.config.artifact_root
        )
       
        return data_ingestion_config