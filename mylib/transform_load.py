"""
This module contains functions to transform and load data into a 
local SQLite3 database. The SQLite3 database is created in the 
current working directory. If the database already exists, it will 
be overwritten.
"""
import sqlite3
import csv


def create_and_load_db(dataset:str="data/GroceryDB_IgFPro.csv", 
                       db_name:str="GroceryDB",
                       sql_conn:sqlite3.Connection=None)->sqlite3.Connection:
    """"function to create a local SQLite3 database and load data into it. 
    The data is transformed from a CSV file."""

    with open(dataset, newline='') as csvfile:
        payload = list(csv.reader(csvfile, delimiter=','))

    column_names = [name if name else 'ID' for name in payload[0]]
    
    if not sql_conn:
        conn = sqlite3.connect(f'{db_name}')
    else:
        conn = sql_conn
    
    c = conn.cursor() # create a cursor
    # drop the table if it exists
    c.execute(f"DROP TABLE IF EXISTS {db_name}") 
    # create the table
    c.execute(f"CREATE TABLE {db_name} ({', '.join(column_names)})")
    # insert the data
    c.executemany(f"INSERT INTO {db_name} VALUES" \
                  f"({', '.join(['?']*len(column_names))})", payload[1:])
    
    conn.commit()
    conn.close()
    
    return conn


if __name__ == '__main__':
    create_and_load_db()
