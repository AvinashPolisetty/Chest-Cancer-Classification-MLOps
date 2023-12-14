from src.Cancerclassifier.config.configuration import ConfigurationManager
from src.Cancerclassifier.components.model_trainer import Training
from src.Cancerclassifier import logger
from exception import CustomException
import sys

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
    
        except Exception as e:
            raise CustomException(e,sys)