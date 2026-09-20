from database.mysqlConnection import connector

class model:
    def get_users():
        conn = connector()
        cursor = conn.cursor()

    def get_message():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM wesson")
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return messages

    




