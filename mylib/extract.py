"""
This module provides functions for extracting data from url to a file path.
The data must be in CSV format.
"""
import requests

def extract(url:str="https://raw.githubusercontent.com/Barabasi-Lab/"
            "GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_path:str="data/GroceryDB_IgFPro.csv")->str:
    """"Extract data from url to a file path. The data must be in CSV format."""
    
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    
    return file_path
