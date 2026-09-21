from database.mysqlConnection import connector

class messageModel():
     def get_message():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM wesson")
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return messages

