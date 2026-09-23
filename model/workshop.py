from database.mysqlConnection import fetch_data, execute_query

def get_all_hosts():
    return fetch_data("SELECT id, host_name FROM hosts")

def get_all_locations():
    return fetch_data("SELECT id, location_name FROM location")

def get_all_workshops():
    return fetch_data("SELECT id, workshop_name FROM workshop")

def create_host(host_name, user_id):
    # Updated to user_id to match your database column name
    query = "INSERT INTO hosts (host_name, user_id) VALUES (%s, %s)"
    execute_query(query, (host_name, user_id))

def create_location(location_name, capacity):
    execute_query("INSERT INTO location (location_name, capacity) VALUES (%s, %s)", (location_name, capacity))

def create_workshop(workshop_name, host_id):
    execute_query("INSERT INTO workshop (workshop_name, hostID) VALUES (%s, %s)", (workshop_name, host_id))

def create_timeslot(workshop_id, session_datetime, is_public, location_id):
    query = "INSERT INTO workshop_time_slot (workshop_id, session_datetime, is_public, location_id) VALUES (%s, %s, %s, %s)"
    execute_query(query, (workshop_id, session_datetime, is_public, location_id))