from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories
class ConfigurationManager:
    def __init__(self):
                 #config_filepath=CONFIG_FILE_PATH,
                 #schema_filepath=SCHEMA_FILE_PATH,
                 #params_filepath=PARAMS_FILE_PATH):
                 
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        self.schema=read_yaml(SCHEMA_FILE_PATH)
        
        create_directories([self.config.artifacts_root]) 
        