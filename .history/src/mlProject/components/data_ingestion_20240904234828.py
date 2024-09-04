import os 
from mlProject import logging
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
        
    def download_file(self):
        if not os.path.exists(self.config.local_path):
            filename,header=request.    