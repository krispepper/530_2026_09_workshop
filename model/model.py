from database.mysqlConnection import connector
from flask import redirect, url_for

class model:
    @staticmethod
    def getUsers():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
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

    
    @staticmethod
    def createMessage():
      conn = connector()
      cursor = conn.cursor()

      cursor.execute("INSERT INTO messages(message) VALUES ('test message'),(message)")

      conn.commit()

      cursor.close()
      conn.close()

    @staticmethod
    def createWorkshop(workshop_name, hostID):
      conn = connector()
      cursor = conn.cursor()

      cursor.execute("INSERT INTO workshop(workshop_name, hostID) VALUES (%s, %s)", (workshop_name, hostID))

      conn.commit()

      cursor.close()
      conn.close()

    @staticmethod
    def getWorkshops():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM workshop")
        workshops = cursor.fetchall()
        cursor.close()
        conn.close()
        return workshops
      
    @staticmethod
    def getHosts():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hosts")
        hosts = cursor.fetchall()
        cursor.close()
        conn.close()
        return hosts

