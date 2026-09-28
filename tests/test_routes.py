from model.model import model


#test for the home route
def test_home_route(client):

    #i will send a GET request to the home route
    response = client.get('/')

    #I then will make sure the response status code is 200
    assert response.status_code == 200



   
    







