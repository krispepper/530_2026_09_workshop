from database.mysqlConnection import fetch_data, execute_query

class model:
    @staticmethod
    def getUsers():
        return fetch_data("SELECT * FROM users")

    @staticmethod
    def getMessage():
        return fetch_data("SELECT * FROM messages")

    @staticmethod
    def createMessage(message_text):
        execute_query("INSERT INTO messages (message) VALUES (%s)", (message_text,))