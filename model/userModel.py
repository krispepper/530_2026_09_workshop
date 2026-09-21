from database.mysqlConnection import connector

class userModel():
    def get_users():
        conn = connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

   
        
        

    




