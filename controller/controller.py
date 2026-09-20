from flask import render_template, request, redirect, url_for
from model.model import model

def test(app):
    @app.route('/')
    def showMessage():
        messages = model.get_message()
        users = model.get_users()
        return render_template('home.html',messages=messages,users=users)
        

        