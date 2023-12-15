from src.Cancerclassifier.config.configuration import ConfigurationManager
from src.Cancerclassifier.components.model_evaluation_with_mlflow import Evaluation
from src.Cancerclassifier import logger
from exception import CustomException
import sys

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()

        except Exception as e:
            raise CustomException(e,sys)
