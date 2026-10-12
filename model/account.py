#Purpose: to find out what workshops a user is enrolled in and diplay them in account.html

from database.mysqlConnection import fetch_data, execute_query

def get_workshops_for_account(user_id):
    query="""SELECT u.id,wr.timeslot_id, wts.workshop_id, w.workshop_name, h.host_name
    FROM users u
    INNER JOIN workshop_roster wr ON u.id = wr.personID
    INNER JOIN workshop_time_slot wts ON wr.timeslot_id = wts.id
    INNER JOIN workshop w on wts.workshop_id = w.id
    INNER JOIN hosts h on w.hostID = h.id
    WHERE u.id = %s"""

    return fetch_data(query, (user_id,))