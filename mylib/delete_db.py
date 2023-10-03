"""This module contains functions to delete a table from a local SQLite3 database."""""
import sqlite3


def drop_table(db_name:str="GroceryDB.db", 
               table_name:str="GroceryDB",
               sql_conn:sqlite3.Connection=None) -> None:
    """function to drop a table from a local SQLite3 database."""
    if not sql_conn:
        conn = sqlite3.connect(db_name)
    else:
        conn = sql_conn
    
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()

    print(f"Table {table_name} dropped from {db_name}.")
