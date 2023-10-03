"""Update the database"""
import sqlite3


def update_db(conn:sqlite3.Connection=None, 
              query_str:str='',
              sql_conn:sqlite3.Connection=None)->None:
    """Update the database"""
    if not conn:
        conn = sqlite3.connect("GroceryDB")

    cursor = conn.cursor()
    
    if query_str == '':
        cursor.execute("UPDATE GroceryDB SET semantic_tree_name = 'Rakeen'"\
                    " WHERE count_products = '11'")
    else:
        cursor.execute(query_str)
    
    conn.commit()

    print("Records updated")


if __name__ == '__main__':
    conn_ = sqlite3.connect("GroceryDB.db")
    update_db(conn_)
    conn_.close()
