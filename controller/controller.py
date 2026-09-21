from flask import render_template
from model.model import model

def viewHome(app):
    @app.route("/")
    def showHome():
        messages = model.getMessage()
        users = model.getUsers()
        return render_template("home.html",messages=messages,users=users)
        #return render_template("test.html",messages=messages)
        

        