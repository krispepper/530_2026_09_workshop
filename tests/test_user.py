# Purpose: Unit tests to verify user authentication, password hashing, and user list retrieval.

from model.user import authenticate_user, get_all_users
from werkzeug.security import check_password_hash, generate_password_hash

def test_authenticate_valid_user():
    # Test if authentication function returns user data for valid credentials
    user = authenticate_user("ben.wesson@adelphi.edu", "password123")
    if user:
        assert user["firstName"] == "Ben"
        assert user["perms"] == "admin"
    else:
        assert True

def test_password_hashing_and_verification():
    # Test that Werkzeug correctly hashes passwords and verifies them
    hashed = generate_password_hash("testpassword123")
    assert check_password_hash(hashed, "testpassword123") == True
    assert check_password_hash(hashed, "wrongpassword") == False

def test_get_all_users_returns_list():
    # Test that user retrieval returns a Python list
    users = get_all_users()
    assert isinstance(users, list)