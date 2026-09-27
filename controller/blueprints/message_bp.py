
from flask import Blueprint, render_template, redirect, request, url_for, flash
from jinja2.exceptions import TemplateNotFound
from model.model import model

message_bp = Blueprint('message', __name__, template_folder='templates')

# Route to handle saving a new message submission
@message_bp.route("/createMessage", methods=["POST"])
def createMessage():
    try:
        message = request.form["message"]
        model.createMessage(message)
        # Flash a success message and redirect to the home page after successfully creating the message
        flash("Message created successfully!")
        return redirect(url_for("home.home"))

    except TemplateNotFound:
        # Redirect to the home page if there is an error rendering the template
        return redirect(url_for('home.home'))

# Route to display the message submission form page
@message_bp.route("/message")
def messageForm():
    try:
        return render_template("message.html")
    except TemplateNotFound:
        # Redirect to the home page if the message submission page is not found
        return redirect(url_for('home.home'))