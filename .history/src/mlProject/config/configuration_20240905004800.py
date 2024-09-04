from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories
import os
from mlProject.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self):
                 #config_filepath=CONFIG_FILE_PATH,
                 #schema_filepath=SCHEMA_FILE_PATH,
                 #params_filepath=PARAMS_FILE_PATH):
                 
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(SCHEMA_FILE_PATH)
        self.schema=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            local_path=config.local_path,
            unzip_dir=config.unzip_dir
        )    
        
        return data_ingestion_config