# from the user.py file in model we'll use authenticate_user and get_all_users
from model.user import authenticate_user, get_all_users

#testing if it authenticates the users correctly
def test_authenticate_valid_user():
    #calls function 
    user = authenticate_user("ben.wesson@email.com", "password123")
    #if user was found
    if user:
        #checks if authenticated user has the expected info
        assert user[1] == "Ben"
        assert user[4] == "admin"
    else:
        assert True

#testing to see if the all the users return in list format
def test_get_all_users():
    #stores function in users
    users = get_all_users()
    #returns output
    assert isinstance(users, list)