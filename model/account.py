#Purpose: to find out what workshops a user is enrolled in and diplay them in account.html

from database.mysqlConnection import fetch_data, execute_query

def get_user_permission(user_id):
    """Fetches the user's permission level from the database."""
    query = "SELECT perms FROM users WHERE id = %s"
    result = fetch_data(query, (user_id,))
    
    # Return the permission string, or default to 'student' if something goes wrong
    return result[0][0] if result else 'student'

def get_workshops_for_account(user_id):
    query="""SELECT u.id,wr.timeslot_id, wts.workshop_id, w.workshop_name, h.host_name
    FROM users u
    INNER JOIN workshop_roster wr ON u.id = wr.personID
    INNER JOIN workshop_time_slot wts ON wr.timeslot_id = wts.id
    INNER JOIN workshop w on wts.workshop_id = w.id
    INNER JOIN hosts h on w.hostID = h.id
    WHERE u.id = %s"""

    return fetch_data(query, (user_id,))

def cancel_enrollment(user_id, timeslot_id):
    # SQL query to remove the user's enrollment record for a specific timeslot
    query = "DELETE FROM workshop_roster WHERE personID = %s AND timeslot_id = %s"
    execute_query(query, (user_id, timeslot_id))

def get_hosted_workshops(user_id):
    # Fetch distinct workshops created by this specific user
    query = """
        SELECT w.id, w.workshop_name
        FROM workshop w
        JOIN hosts h ON w.hostID = h.id
        WHERE h.user_id = %s
    """
    return fetch_data(query, (user_id,))

def get_hosted_timeslots(user_id):
    # Fetch all the individual timeslots for the workshops this user hosts
    query = """
        SELECT w.id, w.workshop_name, ts.id, ts.session_datetime, ts.is_public
        FROM workshop w
        JOIN hosts h ON w.hostID = h.id
        JOIN workshop_time_slot ts ON w.id = ts.workshop_id
        WHERE h.user_id = %s
        ORDER BY ts.session_datetime ASC
    """
    return fetch_data(query, (user_id,))

def delete_timeslot(timeslot_id):
    # Step 1: Delete any private invitations tied to this specific timeslot
    invites_query = "DELETE FROM workshop_invitations WHERE private_timeslot_id = %s"
    execute_query(invites_query, (timeslot_id,))
    
    # Step 2: Delete user enrollments (roster) tied to this specific timeslot
    roster_query = "DELETE FROM workshop_roster WHERE timeslot_id = %s"
    execute_query(roster_query, (timeslot_id,))
    
    # Step 3: Delete the timeslot itself
    timeslot_query = "DELETE FROM workshop_time_slot WHERE id = %s"
    execute_query(timeslot_query, (timeslot_id,))

def delete_workshop(workshop_id):
    # Step 1: Delete all invitations tied to ALL timeslots for this workshop
    invites_query = "DELETE FROM workshop_invitations WHERE private_timeslot_id IN (SELECT id FROM workshop_time_slot WHERE workshop_id = %s)"
    execute_query(invites_query, (workshop_id,))
    
    # Step 2: Delete user enrollments (roster) tied to ALL timeslots for this workshop
    roster_query = "DELETE FROM workshop_roster WHERE timeslot_id IN (SELECT id FROM workshop_time_slot WHERE workshop_id = %s)"
    execute_query(roster_query, (workshop_id,))
    
    # Step 3: Delete the timeslots
    timeslot_query = "DELETE FROM workshop_time_slot WHERE workshop_id = %s"
    execute_query(timeslot_query, (workshop_id,))
    
    # Step 4: Delete the workshop itself
    workshop_query = "DELETE FROM workshop WHERE id = %s"
    execute_query(workshop_query, (workshop_id,))

def get_all_workshops():
    # Fetch every workshop in the database, including the host's name
    query = """
        SELECT w.id, w.workshop_name, h.host_name
        FROM workshop w
        JOIN hosts h ON w.hostID = h.id
    """
    return fetch_data(query)

def get_hosted_workshops(user_id):
    # Fetch distinct workshops created by this specific user, including host's name
    query = """
        SELECT w.id, w.workshop_name, h.host_name
        FROM workshop w
        JOIN hosts h ON w.hostID = h.id
        WHERE h.user_id = %s
    """
    return fetch_data(query, (user_id,))

def get_all_timeslots():
    # Fetch every timeslot in the database for the admin view
    query = """
        SELECT w.id, w.workshop_name, ts.id, ts.session_datetime, ts.is_public
        FROM workshop w
        JOIN workshop_time_slot ts ON w.id = ts.workshop_id
        ORDER BY ts.session_datetime ASC
    """
    return fetch_data(query)