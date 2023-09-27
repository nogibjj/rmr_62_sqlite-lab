"""Query the database"""

import sqlite3
from prettytable import PrettyTable


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
    print("Top 5 rows of the GroceryDB table:")
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = [i[0] for i in cursor.description]
    for row in rows:
        x.add_row(row)
    print(x)
    conn.close()
    return "Success"


