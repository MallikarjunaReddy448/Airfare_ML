import os
import sys 
from src.exception import CustomException
from src import logger
import pandas
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'data.csv')

    

if __name__ == '__main__':
    pass