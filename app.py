from flask import Flask
from controller.controller import test

app = Flask(__name__)
test(app)

