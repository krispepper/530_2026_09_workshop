from database.mysqlConnection import connector

class model:
    @staticmethod
    def getUsers():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `USER`")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

    @staticmethod
    def getMessage():
      conn = connector()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM messages")
      messages = cursor.fetchall()
      cursor.close()
      conn.close()
      return messages