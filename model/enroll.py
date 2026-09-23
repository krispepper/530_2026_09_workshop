# Purpose: Handles workshop enrollment logic, filtering available public sessions and private invitations for each user.

from database.mysqlConnection import fetch_data, execute_query

def get_available_timeslots(user_id):
    # SQL query to fetch public workshops OR private workshops the user is explicitly invited to
    query = """
        SELECT ts.id, w.workshop_name, l.location_name, ts.session_datetime, ts.is_public
        FROM workshop_time_slot ts
        JOIN workshop w ON ts.workshop_id = w.id
        JOIN location l ON ts.location_id = l.id
        WHERE ts.is_public = 1 
           OR ts.id IN (SELECT private_timeslot_id FROM workshop_invitations WHERE userID = %s)
    """
    return fetch_data(query, (user_id,))

def enroll_in_workshop(user_id, timeslot_id):
    # Record the user's enrollment into a specific workshop timeslot in the roster table
    query = "INSERT INTO workshop_roster (personID, timeslot_id) VALUES (%s, %s)"
    execute_query(query, (user_id, timeslot_id))