import sqlite3


def update_db(conn, default_db="GroceryDB"):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {default_db} SET semantic_tree_name = 'Rakeen'"/
                   " WHERE count_products = '11'")
    conn.commit()

    print("Records updated")


if __name__ == '__main__':
    conn_ = sqlite3.connect("GroceryDB.db")
    update_db(conn_)
    pass