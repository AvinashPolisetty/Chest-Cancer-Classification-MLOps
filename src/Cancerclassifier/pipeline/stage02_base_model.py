from src.Cancerclassifier.config.configuration import ConfigurationManager
from src.Cancerclassifier.components.prepare_base_model import PrepareBaseModel
from src.Cancerclassifier import logger
from exception import CustomException
import sys

class PrepareBasemodelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise CustomException(e,sys)
