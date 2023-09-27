"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats 
tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/Barabasi-Lab/"
            "GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_path="data/GroceryDB_IgFPro.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



