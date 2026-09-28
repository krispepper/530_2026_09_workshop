# Purpose: Manages MySQL database connections and provides reusable helper functions to execute read (SELECT) and write (INSERT/UPDATE/DELETE) queries.

import mysql.connector as mys
import getpass

USER = getpass.getuser()
#print(USER)

def connector():
    # Establish and return a connection to the local MySQL database
    return mys.connect(
        host="localhost",
        user=USER,
        database="fall2026_530_workshop",
        ssl_disabled=True
    )

# Reusable module for SELECT queries (Read)
def fetch_data(query, params=None):
    # Connect to database, execute query with optional parameters, fetch all rows, and close connections
    conn = connector()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Reusable module for INSERT/UPDATE/DELETE queries (Write)
def execute_query(query, params=None):
    # Connect to database, execute write query, commit changes, capture last inserted row ID, and close connections
    conn = connector()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    
    # Grab the ID of the row we just inserted
    last_id = cursor.lastrowid 
    
    cursor.close()
    conn.close()
    
    return last_id