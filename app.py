import os
from flask import Flask
from controller.controller import manageRoutes

class App:
    def __init__(self):
        self.app = Flask(__name__)
        # Required for Flask session management (login tracking)
        self.app.secret_key = "super_secret_workshop_key_2026" 
        manageRoutes(self.app)
     
def createApp():
    myFlaskApp = App()
    return myFlaskApp.app

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        user_port = input("Enter Port Number:")
        os.environ["MY_APP_PORT"] = user_port
    
    port_number = int(os.environ.get("MY_APP_PORT"))
    createApp().run(debug=True, port=port_number)