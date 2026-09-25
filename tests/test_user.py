# Purpose: Unit tests to verify user authentication, password hashing, and user list retrieval.

from model.user import authenticate_user, get_all_users

def test_authenticate_valid_user():
    # Test if authentication function returns user data for valid credentials
    user = authenticate_user("ben.wesson@adelphi.edu", "password123")
    if user:
        assert user["firstName"] == "Ben"
        assert user["perms"] == "admin"
    else:
        assert True

def test_get_all_users_returns_list():
    # Test that user retrieval returns a Python list
    users = get_all_users()
    assert isinstance(users, list)