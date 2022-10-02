import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_games_table = """
        CREATE TABLE games (
        name TEXT PRIMARY KEY,
        number INTEGER NOT NULL
        );"""
    
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_games_table)
    else:
        print("Error.")

if __name__ == "__main__":
    main()