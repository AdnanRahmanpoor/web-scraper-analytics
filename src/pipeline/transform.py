import pandas as pd
import numpy as np
import sys

sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')

from src.utils.database import DatabaseConnection

class DataTransform:
    def __init__(self):
        self.df = None

    def load_raw_data(self, file_path):
        "Load raw data CSV or JSON"
        if file_path.endswith('.csv'):
            self.df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            self.df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")