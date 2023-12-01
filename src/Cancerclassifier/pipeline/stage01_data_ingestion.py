from src.Cancerclassifier.config.configuration import ConfigurationManager
from src.Cancerclassifier.components.data_ingestion import DataIngestion
from src.Cancerclassifier import logger
from exception import CustomException


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException