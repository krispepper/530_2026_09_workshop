# Purpose: Manages database queries and operations for user accounts, including user creation, authentication, retrieval, and password updates across normalized tables.

from database.mysqlConnection import fetch_data, execute_query

def get_all_users():
    # Fetch all user records along with their email from the normalized tables
    query = """
        SELECT u.id, u.firstName, u.lastName, e.email, u.perms 
        FROM users u
        LEFT JOIN email e ON u.id = e.personId
    """
    return fetch_data(query)

def authenticate_user(email, password):
    # Retrieve user account details by joining users and email tables for authentication verification
    query = """
        SELECT u.id, u.firstName, u.lastName, e.email, u.password, u.perms 
        FROM users u
        JOIN email e ON u.id = e.personId
        WHERE e.email = %s
    """
    users = fetch_data(query, (email,))
    if users:
        return users[0]
    return None

def create_user(first_name, last_name, email, hashed_password, phone_number, perms):
    # Insert user base details into the users table and retrieve the new user ID
    user_query = "INSERT INTO users (firstName, lastName, password, perms) VALUES (%s, %s, %s, %s)"
    user_id = execute_query(user_query, (first_name, last_name, hashed_password, perms))
    
    # Insert email into the separate email table if provided
    if email and user_id:
        email_query = "INSERT INTO email (email, personId) VALUES (%s, %s)"
        execute_query(email_query, (email, user_id))
        
    # Insert phone number into the separate phonenumber table if provided
    if phone_number and user_id:
        phone_query = "INSERT INTO phonenumber (phonenumber, userID) VALUES (%s, %s)"
        execute_query(phone_query, (phone_number, user_id))

def update_password(user_id, hashed_password):
    # Update the password hash for a specific user ID in the users table
    query = "UPDATE users SET password = %s WHERE id = %s"
    execute_query(query, (hashed_password, user_id))