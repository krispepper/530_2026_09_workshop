
import pytest
from app import createApp

@pytest.fixture
def app():
    app = createApp()
    app.config['TESTING'] = True
    yield app
    #if i were altering database rows i could clean up below my yield statement
    #however, I will just be just performing a get for my home route
    
@pytest.fixture
def client(app):
    #test client for the app
    return app.test_client()


    