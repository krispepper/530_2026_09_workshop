# Purpose: Manages database operations for general application entities such as system users and messages.

from database.mysqlConnection import fetch_data, execute_query

class model:
    @staticmethod
    def getUsers():
        # Retrieve all user records from the users table
        return fetch_data("SELECT * FROM users")

    @staticmethod
    def getMessage():
        # Retrieve all message records from the messages table
        return fetch_data("SELECT * FROM messages")

    @staticmethod
    def createMessage(message_text):
        # Insert a new message text record into the messages table
        execute_query("INSERT INTO messages (message) VALUES (%s)", (message_text,))