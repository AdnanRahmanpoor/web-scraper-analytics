import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

class ProductAnalyzer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.sclaer = StandardScaler()

    def perform_basic_analysis(self):
        """Perform basic statistical analysis"""
        stats = {
            'total_products': len(self.df),
            'price_stats': self.df['price'].describe().to_dict(),
            'categories': self.df['category'].value_counts().to_dict(),
            'price_correlation': self.calculate_correlation()
        }
        return stats
    
    