from flask import Blueprint, render_template, redirect, abort
from jinja2.exceptions import TemplateNotFound
from model.model import model
from model import user


home_bp = Blueprint('home', __name__,template_folder='templates')

# Route for the home dashboard displaying system messages and user list
@home_bp.route('/')
def home():

    try:
        messages = model.getMessage()
        users = user.get_all_users() 
        return render_template('home.html', messages=messages, users=users)
        
    except TemplateNotFound:
    #if we can't render the home page, return a 404 error
        abort(404)