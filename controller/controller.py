from flask import render_template
from model.messageModel import messageModel
from model.userModel import userModel

def viewHome(app):
    @app.route("/")
    def showHome():
        messages = messageModel.get_message()
        users = userModel.get_users()
        return render_template("home.html",messages=messages,users=users)
        

        