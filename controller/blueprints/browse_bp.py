from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from jinja2.exceptions import TemplateNotFound
from model import enroll



# Route to display available workshop slots for the logged-in user to enroll
browse_bp = Blueprint('browse', __name__, template_folder='templates')
@browse_bp.route("/browse", methods=["GET"])
def showEnroll():

    try:
        workshops = enroll.get_workshop_details_joined()
        return render_template("browse.html", workshops = workshops)

    except TemplateNotFound:
        flash("Enrollment page not found.")
        # Redirect to the home page if the enrollment page is not found
        return redirect(url_for("home.home"))
