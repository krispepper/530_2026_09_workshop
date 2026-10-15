# Purpose: Handles logic for inbox

from database.mysqlConnection import fetch_data, execute_query

def get_inbox_messages():
    # SQL query to fetch public workshops OR private workshops the user is explicitly invited to
    query = """
        SELECT im.id, im.personID, im.timeslot_id, im.created_at, w.workshop_name, u.firstName, e.email
        FROM inbox_messages im
        INNER JOIN workshop_time_slot wts ON im.timeslot_id
        INNER JOIN workshop w ON wts.workshop_id = w.id
        INNER JOIN users u ON im.personID = u.id
        INNER JOIN email e ON u.id = e.personID
    """
    return fetch_data(query)

def create_invite_request(personID,timeslot_id):
    query= """
        INSERT INTO inbox_messages(personID,timeslot_id)
        VALUES(%s,%s)
    """
    return execute_query(query,(personID,timeslot_id,))