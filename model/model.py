from database.mysqlConnection import connector

class model:
    conn = connector()
    cursor = conn.cursor()