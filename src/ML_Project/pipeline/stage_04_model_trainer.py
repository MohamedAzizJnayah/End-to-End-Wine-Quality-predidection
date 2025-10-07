


from ML_Project.components.model_trainer import ModelTrainer
from ML_Project.config.configuration import ConfigurationManager
from ML_Project.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    obj=ModelTrainerPipeline()
    obj.main()
