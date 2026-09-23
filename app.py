# Purpose: Entry point for the Flask application using an Object-Oriented structure, supporting dynamic port input and session management.

import os
from flask import Flask
from controller.controller import manageRoutes

class App:
    def __init__(self):
        # Initialize the Flask application instance
        self.app = Flask(__name__)
        # Required for Flask session management (login tracking)
        self.app.secret_key = "super_secret_workshop_key_2026" 
        # Register all application routes from the controller module
        manageRoutes(self.app)
     
def createApp():
    # Factory function to create and return the Flask app instance
    myFlaskApp = App()
    return myFlaskApp.app

if __name__ == "__main__":
    # Prompt the user for a port number when starting the app (bypassing reloader prompts)
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        user_port = input("Enter Port Number:")
        os.environ["MY_APP_PORT"] = user_port
    
    # Retrieve the configured port number and run the Flask application in debug mode
    port_number = int(os.environ.get("MY_APP_PORT"))
    createApp().run(debug=True, port=port_number)