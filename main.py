from src.Cancerclassifier import logger
from exception import CustomException
import sys
from src.Cancerclassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.Cancerclassifier.pipeline.stage02_base_model import PrepareBasemodelPipeline


stage_name="Data Ingestion Stage"

try:
    logger.info(f"<<<<<<<<  {stage_name} started  >>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<  {stage_name} completed  >>>>>>>>")
except Exception as e:
    raise CustomException(e,sys)


stage_name="Prepare Base Model Stage"

try:
    logger.info(f"<<<<<<<<  {stage_name} started  >>>>>>>>")
    obj=PrepareBasemodelPipeline()
    obj.main()
    logger.info(f"<<<<<<<<  {stage_name} completed  >>>>>>>>")
except Exception as e:
    raise CustomException(e,sys)



