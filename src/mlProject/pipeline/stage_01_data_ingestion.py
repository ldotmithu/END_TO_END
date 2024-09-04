
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logging

Stage_name='Data_Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.det_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()    
try:
    obj=DataIngestionTrainingPipeline()
    obj.main()
except Exception as e:
    logging.exception(e)
    raise e  