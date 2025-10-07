import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from ML_Project.logging import logger
from ML_Project.entity.config_entity import ModelEvaluationConfig
from ML_Project.utils.common import save_json
import pandas as pd

class ModelEvaluation :
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config


    def eval_metrics(self):
        
        try:
            X_test=pd.read_csv(self.config.test_data_path).drop(columns=[str(self.config.target_column.name)],axis=1)
            y_test=pd.read_csv(self.config.test_data_path)[[str(self.config.target_column.name)]]
            model_evaluation=joblib.load(self.config.model_path)
            predicted_results=model_evaluation.predict(X_test)


            mse=mean_squared_error(y_test,predicted_results)
            mae=mean_absolute_error(y_test,predicted_results)
            r2=r2_score(y_test,predicted_results)
            data={
                "mse":mse,
                "mae":mae,
                "r2":r2
            }
        #~Save Json
            save_json(data,self.config.metrics_file_name)
            logger.info(f"Evaluation Metrics are in this Path at : {self.config.metrics_file_name}")
        except Exception as e:
            logger.error("Error in eval metrics Function")
            raise e
    