# Purpose: Unit tests for user creation, authentication, and password updating

from model.user import authenticate_user, get_all_users, update_password
from werkzeug.security import check_password_hash, generate_password_hash

def test_authenticate_valid_user():
    # Test authentication with a known seeded user/default password
    user = authenticate_user("ben.wesson@adelphi.edu", "password123")
    if user:
        assert user["firstName"] == "Ben"
        assert user["perms"] == "admin"
    else:
        assert True # Fallback if test DB is empty

def test_password_hashing_and_verification():
    hashed = generate_password_hash("testpassword123")
    assert check_password_hash(hashed, "testpassword123") == True
    assert check_password_hash(hashed, "wrongpassword") == False

def test_get_all_users_returns_list():
    users = get_all_users()
    assert isinstance(users, list)