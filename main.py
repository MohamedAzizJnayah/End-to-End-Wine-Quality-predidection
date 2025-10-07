from  ML_Project.logging import logger
from ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ML_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ML_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingTransformation
from ML_Project.pipeline.stage_04_model_trainer import ModelTrainerPipeline

try:
        STAGE_NAME="Data Ingestion Stage"
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



try:
        STAGE_NAME="Data Validation Stage"
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj2=DataValidationTrainingPipeline()
        obj2.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


try:
        STAGE_NAME="Data Transformation Stage"
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj3=DataTransformationTrainingTransformation()
        obj3.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


try:
        STAGE_NAME="Model Trainer Stage"
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj3=ModelTrainerPipeline()
        obj3.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e