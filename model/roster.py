from database.mysqlConnection import fetch_data, execute_query

def get_roster(timeslot_id):
    query = """
        SELECT wr.personID, wr.timeslot_id, u.firstName, u.lastName, u.perms, wts.workshop_id, h.host_name, w.workshop_name
        FROM workshop_roster wr
        INNER JOIN users u ON wr.personID = u.id
        INNER JOIN workshop_time_slot wts ON wr.timeslot_id = wts.id
        INNER JOIN workshop w ON wts.workshop_id = w.id
        INNER JOIN hosts h ON w.hostID = h.id
        WHERE timeslot_id = %s
    """
    return fetch_data(query, (timeslot_id,))

   

    