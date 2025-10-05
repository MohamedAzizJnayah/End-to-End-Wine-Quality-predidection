#Configuration Manager

from ML_Project.constants import *
from ML_Project.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig
from ML_Project.utils.common import create_directories


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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        root_dir=Path(config.root_dir)
        create_directories([root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=Path(config.root_dir),
            unzip_data_dir=Path(config.unzip_data_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            all_schema=self.schema
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config=self.config.data_transformation
        root_dir=Path(config.root_dir)
        create_directories([root_dir])
        data_transformation_config=DataTransformationConfig(
            root_dir=root_dir,
            data_path=Path(config.data_path)
        )
        return data_transformation_config