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

    def clean_data(self):
        """Clean and preprocess the data"""
        if self.df is None:
            raise ValueError("No data loaded")

        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Handle missing values
        self.df.fillna({
            'description': 'No description available',
            'category': 'Uncategorized'
        }, inplace=True)

        # Clean price data
        self.df['price'] = pd.to_numeric(self.df['price'].astype(str).str.replace('$', ''),
            error='coerce')

        # Convert timestamps
        if 'created_at' in self.df.columns:
            self.df['created_at'] = pd.to_datetime(self.df['created_at'])

    def tranform_for_analysis(self):
        """Apply transformation for analysis"""
        if self.df is None:
            raise ValueError("No data loaded")

        # Add derived features
        self.df['price_category'] = pd.qcut(self.df['price'],
            q=4,
            labels=['Budget', 'Medium', 'High', 'Premium']) # placeholder for now

        # Calculate basic statistics
        self.df['price_normalized'] = (self.df['price'] - self.df['price'].mean()) / self.df['price'].std()