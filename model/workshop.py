#from database.mysqlConnection import connector
import mysql.connector as mys
from datetime import datetime

def connector():
    conn = mys.connect(
        host="localhost",
        user="benjaminwesson",
        database="fall2026_530_workshop",
        ssl_disabled=True
    )
    return conn

def get_host(connector):
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, host_name FROM hosts")
    result = cursor.fetchall()
    
    print("\n--- Existing Hosts ---")
    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]}")
        
    while True:
        try:
            host_id = int(input("Enter the ID of the host you want to select: "))
            cursor.close()
            conn.close()
            return host_id
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_host(connector):
    conn = connector()
    cursor = conn.cursor()
    host_name = input("Enter the name of the new host: ")
    
    query = "INSERT INTO hosts (host_name) VALUES (%s)"
    cursor.execute(query, (host_name,))
    conn.commit()
    
    host_id = cursor.lastrowid
    print(f"Success! Host '{host_name}' created with ID: {host_id}")
    
    cursor.close()
    conn.close()
    return host_id

def get_location(connector):
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, location_name FROM location")
    result = cursor.fetchall()
    
    print("\n--- Existing Locations ---")
    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]}")
        
    while True:
        try:
            location_id = int(input("Enter the ID of the location you want to select: "))
            cursor.close()
            conn.close()
            return location_id
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_location(connector):
    conn = connector()
    cursor = conn.cursor()
    location_name = input("Enter the name of the new location: ")
    
    while True:
        try:
            capacity = int(input("Enter the capacity for this location (number only): "))
            break
        except ValueError:
            print("Invalid capacity. You must enter a number.")

    query = "INSERT INTO location (location_name, capacity) VALUES (%s, %s)"
    cursor.execute(query, (location_name, capacity))
    conn.commit()
    
    location_id = cursor.lastrowid
    print(f"Success! Location '{location_name}' created with ID: {location_id}")
    
    cursor.close()
    conn.close()
    return location_id

def get_workshop(connector):
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SELECT id, workshop_name FROM workshop")
    result = cursor.fetchall()
    
    print("\n--- Existing Workshops ---")
    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]}")
        
    while True:
        try:
            workshop_id = int(input("Enter the ID of the workshop you want to select: "))
            cursor.close()
            conn.close()
            return workshop_id
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_workshop(connector):
    # First, select an existing host to link to this workshop
    print("\n[Step 1 of 2: Select a Host for this Workshop]")
    host_id = get_host(connector)

    conn = connector()
    cursor = conn.cursor()

    while True:
        workshop_name = input("\n[Step 2 of 2] Enter the name of the new workshop: ")
        query = "INSERT INTO workshop (workshop_name, hostID) VALUES (%s, %s)"
        
        try:
            cursor.execute(query, (workshop_name, host_id))
            conn.commit()
            
            workshop_id = cursor.lastrowid
            query_select = "SELECT workshop.id, workshop_name, hosts.host_name FROM workshop JOIN hosts ON workshop.hostID = hosts.id WHERE workshop.id = %s"
            cursor.execute(query_select, (workshop_id,))
            result = cursor.fetchone()
            
            print(f"\nSuccess! Workshop Created: {result}")
            break
            
        except mys.IntegrityError:
            print("Error: That workshop name already exists in the database. Please try a different name.")
            
    cursor.close()
    conn.close()
    return workshop_id

def create_workshop_timeslots(connector):
    # First, select an existing workshop
    print("\n[Step 1 of 3: Select a Workshop]")
    workshop_id = get_workshop(connector)

    # Next, select an existing location
    print("\n[Step 2 of 3: Select a Location]")
    location_id = get_location(connector)

    conn = connector()
    cursor = conn.cursor()

    print("\n[Step 3 of 3: Enter Time Slot Details]")
    while True:
        date_time_str = input("Enter the start time for timeslot (Follow format YYYY-MM-DD HH:MM:SS): ")
        try:
            date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
            break
        except ValueError:
            print("Error: Invalid date format. Make sure you use dashes and colons exactly as shown.")

    public = input("Is timeslot public? (yes/no): ").strip().lower()
    is_public = True if public == "yes" else False

    query = "INSERT INTO workshop_time_slot (workshop_id, session_datetime, is_public, location_id) VALUES (%s, %s, %s, %s)"
    values = (workshop_id, date_time, is_public, location_id)

    cursor.execute(query, values)
    conn.commit()
    timeslot_id = cursor.lastrowid

    query_select = """
    SELECT wts.workshop_id, wts.session_datetime, wts.is_public, hosts.host_name, loc.location_name 
    FROM workshop_time_slot AS wts 
    JOIN location AS loc ON wts.location_id = loc.id 
    JOIN workshop AS w ON wts.workshop_id = w.id 
    JOIN hosts ON w.hostID = hosts.id 
    WHERE wts.id = %s
    """
    cursor.execute(query_select, (timeslot_id,))
    result = cursor.fetchone()
    
    print(f"\nSuccess! Timeslot Created: {result}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n===============================")
        print("    WORKSHOP MANAGEMENT MENU   ")
        print("===============================")
        print("1. Create a new Host")
        print("2. Create a new Location")
        print("3. Create a new Workshop")
        print("4. Create a new Workshop Time Slot")
        print("5. Exit Program")
        print("===============================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            create_host(connector)
        elif choice == "2":
            create_location(connector)
        elif choice == "3":
            create_workshop(connector)
        elif choice == "4":
            create_workshop_timeslots(connector)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")