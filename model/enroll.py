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

def get_top_subscribed_workshops(limit=5):
    """
    Fetches the top subscribed public workshops.
    - Groups by workshop to show the count of available timeslots.
    - Only counts timeslots starting from tomorrow onward.
    - Excludes timeslots that are full.
    """
    query = """
        SELECT 
            w.id,
            w.workshop_name,
            COALESCE(h.host_name, 'Instructor TBA') AS host_name,
            COUNT(DISTINCT ts.id) AS available_timeslots,
            (SELECT COUNT(*) FROM workshop_roster wr 
             JOIN workshop_time_slot wts ON wr.timeslot_id = wts.id 
             WHERE wts.workshop_id = w.id) AS total_subscribers
        FROM workshop w
        JOIN workshop_time_slot ts ON w.id = ts.workshop_id
        JOIN location l ON ts.location_id = l.id
        LEFT JOIN hosts h ON w.hostID = h.id
        WHERE ts.is_public = 1
          AND ts.session_datetime >= CURDATE() + INTERVAL 1 DAY
          AND (l.capacity - (SELECT COUNT(*) FROM workshop_roster r WHERE r.timeslot_id = ts.id)) > 0
        GROUP BY w.id, w.workshop_name, h.host_name
        ORDER BY total_subscribers DESC
        LIMIT %s
    """
    return fetch_data(query, (limit,))

def enroll_in_workshop(user_id, timeslot_id):
    # Record the user's enrollment into a specific workshop timeslot in the roster table
    query = "INSERT INTO workshop_roster (personID, timeslot_id) VALUES (%s, %s)"
    execute_query(query, (user_id, timeslot_id))