from dataclasses import dataclass
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
import pandas as pd

@dataclass
class DataIngestionConfig:
    ''' Data Ingestion Configuration 
        We need to create all artifacts because, we may be reading them from an external data source
    '''
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Initiating Data Ingestion")
        try:
            df = pd.read_csv('src/data/HREmployee_data.csv')
            logging.info("Data Ingestion Successful")
            os.makedirs(os.path.join(os.path.dirname(self.config.raw_data_path)), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False, header=True)

            logging.info("Train Test Split Initiated")
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)
            logging.info("Train Test Split Successful")
        except Exception as e:
            raise CustomException(e,sys) from e

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()