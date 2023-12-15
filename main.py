from src.Cancerclassifier import logger
from exception import CustomException
import sys
from src.Cancerclassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.Cancerclassifier.pipeline.stage02_base_model import PrepareBasemodelPipeline
from src.Cancerclassifier.pipeline.stage03_model_trainer import ModelTrainingPipeline
from src.Cancerclassifier.pipeline.stage04_model_evaluation import EvaluationPipeline

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


stage_name="Model training Stage"

try:
    logger.info(f"<<<<<<<<  {stage_name} started  >>>>>>>>")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<  {stage_name} completed  >>>>>>>>")
except Exception as e:
    raise CustomException(e,sys)


stage_name="Model Evaluation Stage"

try:
    logger.info(f"<<<<<<<<  {stage_name} started  >>>>>>>>")
    obj=EvaluationPipeline()
    obj.main()
    logger.info(f"<<<<<<<<  {stage_name} completed  >>>>>>>>")
except Exception as e:
    raise CustomException(e,sys)
