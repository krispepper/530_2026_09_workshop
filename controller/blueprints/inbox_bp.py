#Purpose render tempaltes related to viewing workshop content
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import inbox
from jinja2.exceptions import TemplateNotFound


inbox_bp = Blueprint('inbox', __name__, template_folder='templates')
# Route to handle saving a user's workshop enrollment
@inbox_bp.route("/inbox", methods=["GET"])
def showInbox():
    try: 
        messages = inbox.get_inbox_messages()
        return render_template("inbox.html",messages = messages)

    except TemplateNotFound:
        # Redirect to the home page if there is an error rendering the template
        return redirect(url_for('home.home'))
        