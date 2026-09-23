from database.mysqlConnection import connector

def get_all_hosts():
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, host_name FROM hosts")
    hosts = cursor.fetchall()
    cursor.close()
    conn.close()
    return hosts

def get_all_locations():
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, location_name FROM location")
    locations = cursor.fetchall()
    cursor.close()
    conn.close()
    return locations

def get_all_workshops():
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, workshop_name FROM workshop")
    workshops = cursor.fetchall()
    cursor.close()
    conn.close()
    return workshops

def create_host(host_name):
    conn = connector()
    cursor = conn.cursor()
    query = "INSERT INTO hosts (host_name) VALUES (%s)"
    cursor.execute(query, (host_name,))
    conn.commit()
    cursor.close()
    conn.close()

def create_location(location_name, capacity):
    conn = connector()
    cursor = conn.cursor()
    query = "INSERT INTO location (location_name, capacity) VALUES (%s, %s)"
    cursor.execute(query, (location_name, capacity))
    conn.commit()
    cursor.close()
    conn.close()

def create_workshop(workshop_name, host_id):
    conn = connector()
    cursor = conn.cursor()
    query = "INSERT INTO workshop (workshop_name, hostID) VALUES (%s, %s)"
    cursor.execute(query, (workshop_name, host_id))
    conn.commit()
    cursor.close()
    conn.close()

def create_timeslot(workshop_id, session_datetime, is_public, location_id):
    conn = connector()
    cursor = conn.cursor()
    query = "INSERT INTO workshop_time_slot (workshop_id, session_datetime, is_public, location_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (workshop_id, session_datetime, is_public, location_id))
    conn.commit()
    cursor.close()
    conn.close()