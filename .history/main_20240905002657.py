from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject import logging

Stage_name='Data Inhestion'

try:
    obj=DataIngestionTrainingPipeline()
    obj.main()
except Exception as e:
    logging.exception(e)
    raise e
    
