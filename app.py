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
    createApp().run(debug=True)