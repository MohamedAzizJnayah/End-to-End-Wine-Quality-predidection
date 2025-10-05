from  ML_Project.logging import logger
from ML_Project.pipeline.stage_01_data_ingestion import STAGE_NAME, DataIngestionTrainingPipeline
from ML_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME="Data Validation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj2=DataValidationTrainingPipeline()
        obj2.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e