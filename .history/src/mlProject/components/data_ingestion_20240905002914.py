import os
import urllib.request as request
import zipfile
from mlProject import logging
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
        
    def download_file(self):
        if os.path.exists(self.config.local_path):
            logging.info('file already exists')
            
        else:
            request.urlretrieve(self.config.URL,self.config.local_path)
            logging.info('file Downloaded')       
            
            
    def extract_zip(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_path,'r') as zip_ref:
            zip_ref.extractall(unzip_path)        