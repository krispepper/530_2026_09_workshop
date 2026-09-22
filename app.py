#We used AI assitance to help rewrite our port number setup. 
#Because we wanted to allow multiple group memebers to be on different ports and to have it be a true live server with the debug tag
#This introduced a level of complexity that was above our knowledge level and it was not a core part of our delvierable.
#We used AI for this as more of a quality of life feature.
#We inputed our old set up createApp().run(debug=True, port=5001) as the prompt and asked for a way to have port by user input with persving the live server feature..

import os
from flask import Flask
from controller.controller import viewHome
class App:
    def __init__(self):
        self.app = Flask(__name__)
        viewHome(self.app)
     
def createApp():
    myFlaskApp = App()
    return myFlaskApp.app

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        user_port = input("Enter Port Number:")
        os.environ["MY_APP_PORT"] = user_port
    
    port_number = int(os.environ.get("MY_APP_PORT"))
    createApp().run(debug=True, port=port_number)