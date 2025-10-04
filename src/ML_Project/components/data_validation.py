#Create a Validation Component
from ML_Project.entity.config_entity import DataValidationConfig
from ML_Project.logging import logger
import pandas as pd


class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config=config

    def validate_data_columns(self):
        # Implement validation logic here
        try:
            df=pd.read_csv(self.config.unzip_data_dir)
            expected_columns=self.config.all_schema["COLUMNS"]
            for column in expected_columns:
                if column not in df.columns:
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {column}: FAILED")
                    logger.info(f"Column {column} is missing in the data.")
                    return
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Validation Status: PASSED")
                logger.info("All columns are present in the data.")
        except Exception as e:
            logger.error(f"Error during column validation: {e}")
            raise e

    def validate_data_types(self):
        try:
            df=pd.read_csv(self.config.unzip_data_dir)
            expected_dtypes=self.config.all_schema["COLUMNS"]
            for col,dtype in df.dtypes.items():
                if str(dtype) != expected_dtypes.get(col) and (col != "Id"):
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write("Validation Status: FAILED")
                    logger.info(f"Data type mismatch for column {col}: expected {expected_dtypes.get(col)}, got {dtype}")
                    return

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Validation Status: PASSED")
        except Exception as e:
            logger.error(f"Error during data type validation: {e}")
            raise e