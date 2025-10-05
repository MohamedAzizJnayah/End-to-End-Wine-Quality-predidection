import os
import pandas as pd
from sklearn.model_selection import train_test_split    
from ML_Project.entity.config_entity import DataTransformationConfig
from ML_Project.logging import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        # Implement your train-test split logic here
        try:
            df=pd.read_csv(self.config.data_path)
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            train_data.to_csv(os.path.join(self.config.root_dir, "train_data.csv"), index=False)
            test_data.to_csv(os.path.join(self.config.root_dir, "test_data.csv"), index=False)
            logger.info("Train-test split completed successfully.")
            logger.info(f"Train data shape: {train_data.shape}")
            logger.info(f"Test data shape: {test_data.shape}")
            return train_data, test_data
        except Exception as e:
            logger.error(f"Error occurred while splitting data: {e}")
            return None, None
