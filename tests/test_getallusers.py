from model.user import get_all_users

def test_get_all_users_returns_list():
    # Test that user retrieval returns a Python list
    users = get_all_users()
    assert isinstance(users, list)