


from ML_Project.logging import logger
from ML_Project.components.data_transformation import DataTransformation
from ML_Project.config.configuration import ConfigurationManager


class DataTransformationTrainingTransformation:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager=ConfigurationManager()
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
            return data_transformation
        except Exception as e:
            logger.info(f"Exception occured in stage_03_data_transformation: {e}")  
            raise e
    
if __name__ == "__main__":
    try:
        obj=DataTransformationTrainingTransformation()
        obj.main()
    except Exception as e:
        raise e