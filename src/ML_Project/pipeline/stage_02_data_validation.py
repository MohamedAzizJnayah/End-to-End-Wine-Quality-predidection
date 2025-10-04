from ML_Project.logging import logger
from ML_Project.components.data_validation import DataValidation
from ML_Project.config.configuration import ConfigurationManager

STAGE_NAME="Data Validation Stage"
class DataValidationTrainingPipeline:
    def __init__(self):
         pass
    
    def main(self):
        try:
            config_manager=ConfigurationManager()
            data_validation_config=config_manager.get_data_validation_config()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_data_columns()
            data_validation.validate_data_types()
        except Exception as e:
            logger.error(f"Error in Data Validation: {e}")
            raise e


if __name__ == "__main__":
     
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    