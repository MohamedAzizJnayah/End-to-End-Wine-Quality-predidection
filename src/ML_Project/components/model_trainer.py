
import os
import joblib
from sklearn.linear_model import ElasticNet
import pandas as pd
from ML_Project.logging import logger

from ML_Project.entity.config_entity import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path)
            X_train=train_data.drop(columns=[self.config.target_column],axis=1)
            y_train=train_data[self.config.target_column]
            model=ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio)
            model.fit(X_train,y_train) 
            os.makedirs(self.config.root_dir, exist_ok=True)
            joblib.dump(model,os.path.join(self.config.root_dir,self.config.model_name))
            logger.info(f"Model Trained and saved at {os.path.join(self.config.root_dir,self.config.model_name)}")

        except Exception as e:
            logger.error(f"Error occurred while training model: {e}")
            
     
