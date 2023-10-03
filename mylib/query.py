"""Query the database"""

import sqlite3
from prettytable import PrettyTable


def print_pretty_table(cursor):
    """Print a pretty table from a cursor object"""
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = [i[0] for i in cursor.description]
    for row in rows:
        x.add_row(row)

    print(x)

def query(query_str:str='', db_name:str='GroceryDB.db', 
           ) -> str:
    """Query the database"""
    if not sql_conn:
        conn = sqlite3.connect(db_name)
    else:
        conn = sql_conn
    cursor = conn.cursor()
    
    if query_str == '':
        cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
        print("Top 5 rows of the GroceryDB table:")
        print_pretty_table(cursor)

        cursor.execute("SELECT * FROM GroceryDB where count_products = '11'")
        print("Rows where count_products = '11':")
        print_pretty_table(cursor)

    else:
        cursor.execute(query_str)
        print(f"QUERY: {query_str}")
        print("Query results:")
        print_pretty_table(cursor)

    conn.close()
    
    return "Success"
