import mysql.connector as mys

def connector():
    return mys.connect(
        host="localhost",
        user="benjaminwesson",
        database="fall2026_530_workshop",
        ssl_disabled=True
    )

# Reusable module for SELECT queries (Read)
def fetch_data(query, params=None):
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
    conn = connector()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()