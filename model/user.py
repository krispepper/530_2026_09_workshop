from database.mysqlConnection import fetch_data, execute_query
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(first_name, last_name, perms, email, phone, password):
    hashed_password = generate_password_hash(password)

    user_query = "INSERT INTO users (firstName, lastName, perms, password) VALUES (%s, %s, %s, %s)"
    user_id = execute_query(user_query, (first_name, last_name, perms, hashed_password))

    email_query = "INSERT INTO email (email, personId) VALUES (%s, %s)"
    execute_query(email_query, (email, user_id))

    # 3. Insert into phonenumber table if provided (using any dummy/provided number)
    if phone:
        phone_query = "INSERT INTO phonenumber (phonenumber, userId) VALUES (%s, %s)"
        execute_query(phone_query, (phone, user_id))

def authenticate_user(email, password):
    query = """
        SELECT u.id, u.firstName, u.lastName, u.perms, u.password 
        FROM users u
        JOIN email e ON u.id = e.personId
        WHERE e.email = %s
    """
    result = fetch_data(query, (email,))
    
    if result:
        user = result[0]
        stored_password_hash = user[4]
        if check_password_hash(stored_password_hash, password):
            return {"id": user[0], "firstName": user[1], "lastName": user[2], "perms": user[3]}
            
    return None

def get_all_users():
    return fetch_data("SELECT * FROM users")

def update_password(user_id, new_password):
    hashed_password = generate_password_hash(new_password)
    query = "UPDATE users SET password = %s WHERE id = %s"
    execute_query(query, (hashed_password, user_id))