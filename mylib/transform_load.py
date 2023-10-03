"""
This module contains functions to transform and load data into a 
local SQLite3 database. The SQLite3 database is created in the 
current working directory. If the database already exists, it will 
be overwritten.
"""
import sqlite3
import csv


def create_and_load_db(dataset="data/GroceryDB_IgFPro.csv", db_name="GroceryDB.db"):
    """"function to create a local SQLite3 database and load data into it. 
    The data is transformed from a CSV file."""

    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    
    # skip the header
    column_names = [name if name else 'ID' for name in next(payload)]
    
    conn = sqlite3.connect('GroceryDB.db')
    
    c = conn.cursor() # create a cursor
    # drop the table if it exists
    c.execute(f"DROP TABLE IF EXISTS {db_name}") 
    # create the table
    c.execute(f"CREATE TABLE {db_name} ({', '.join(column_names)})")
    # insert the data
    c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    
    conn.commit()
    conn.close()
    
    return conn
