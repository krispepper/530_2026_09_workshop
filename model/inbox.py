# Purpose: Handles logic for inbox

from database.mysqlConnection import fetch_data, execute_query

def get_inbox_messages():
    # SQL query to fetch public workshops OR private workshops the user is explicitly invited to
    query = """
        SELECT id, personID, timeslot_id, created_at
        FROM inbox_messages
    """
    return fetch_data(query)