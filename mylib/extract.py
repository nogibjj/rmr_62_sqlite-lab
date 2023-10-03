"""
This module provides functions for extracting data from url to a file path.
The data must be in CSV format.
"""
import pandas as pd

def extract(url:str="https://raw.githubusercontent.com/Barabasi-Lab/"
            "GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_path:str="data/GroceryDB_IgFPro.csv")->str:
    """"Extract data from url to a file path. The data must be in CSV format."""
    
    pd.read_html(url)[0].to_csv(file_path, index=False)
    
    return file_path
