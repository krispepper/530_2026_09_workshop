from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from jinja2.exceptions import TemplateNotFound
from model import enroll

enroll_bp = Blueprint('enroll', __name__, template_folder='templates')

# Route to display available workshop slots for the logged-in user to enroll
@enroll_bp.route("/enroll", methods=["GET"])
def showEnroll():

    try:
        if "user_id" not in session:
            flash("Please log in first to enroll in workshops.")
            
            # Redirect to the login page if the user is not logged in
            return redirect(url_for("user.login"))
        user_id = session["user_id"]
        slots = enroll.get_available_timeslots(user_id)
        return render_template("enroll.html", slots=slots)

    except TemplateNotFound:
        flash("Enrollment page not found.")
        # Redirect to the home page if the enrollment page is not found
        return redirect(url_for("home.home"))

# Route to handle saving a user's workshop enrollment
@enroll_bp.route("/createEnrollment", methods=["POST"])
def createEnrollment():
    try:
        user_id = session["user_id"]
        timeslot_id = request.form["timeslot_id"]
        enroll.enroll_in_workshop(user_id, timeslot_id)
        flash("Successfully enrolled in the workshop.")
        # Redirect to the home page after successful enrollment
        return redirect(url_for("home.home"))

    except TemplateNotFound:
        flash("Enrollment page not found.")
        # Redirect to the home page if the enrollment page is not found
        return redirect(url_for("home.home"))