from flask import render_template, request, redirect, url_for
from model.messageModel import messageModel
from model.userModel import userModel

def test(app):
    @app.route('/')
    def showMessage():
        messages = messageModel.get_message()
        users = userModel.get_users()
        return render_template('home.html',messages=messages,users=users)
        

        