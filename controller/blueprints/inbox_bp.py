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
        
@inbox_bp.route("/createInviteRequest", methods=["POST"])
def sendInviteRequest():
    try:
        # SAFETY CHECK: Prevent the KeyError if they somehow get here without logging in
        if "user_id" not in session:
            flash("Please log in first to enroll in workshops.")
            return redirect(url_for("user.login"))
            
        user_id = session["user_id"]
        timeslot_id = request.form["timeslot_id"]
        inbox.create_invite_request(user_id,timeslot_id)
        flash("Invite request sent!")
        
    except: 
        flash("An error occured when requesting for an invite!")

    return redirect(url_for("browse.showEnroll"))
    
    