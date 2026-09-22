#from database.mysqlConnection import connector
import mysql.connector as mys
from datetime import datetime
#this is a temp fucntion to just make this file run individually 
#once we finalize this function we can remove the db connection fucntion
def connector():
    conn = mys.connect(
        host="localhost",
        user="benjaminwesson",
        database="fall2026_530_workshop",
        ssl_disabled=True
    )

    return conn

def get_hosts(connector):
    conn = connector()
    cursor = conn.cursor()

    query = "SELECT * FROM hosts"
    cursor.execute(query)
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()

    print(result)

    id = int(input("Enter the ID of the host you want to select: "))
    print(result[id - 1][1])
    host_id = result[id - 1][0]

    return host_id

def get_location(connector):
    conn = connector()
    cursor = conn.cursor()

    query = "SELECT id, location_name FROM location"
    cursor.execute(query)
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()

    print(result)

    id = int(input("Enter the ID of the location you want to select: "))
    location_name = result[id - 1][1]
    
    return location_name

def create_workshop(connector, host_id):
    conn = connector()
    cursor = conn.cursor()

    workshop_name = input("Enter the name of the workshop: ")

    query = "INSERT INTO workshop (workshop_name, hostID) VALUES (%s, %s)"
    values = (workshop_name, host_id)

    cursor.execute(query, values)
    conn.commit()

    query = "SELECT workshop_name, hosts.host_name FROM workshop JOIN hosts ON workshop.hostID = hosts.id ORDER BY workshop.id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

if __name__ == "__main__":
    host_id = get_hosts(connector)
    #location_name = get_location(connector)
    print(host_id)
    #print(location_name)
    workshop_details = create_workshop(connector, host_id)
    print(workshop_details)