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
        workshops = enroll.get_workshop_details_joined()
        return render_template("enroll.html", workshops = workshops)

    except TemplateNotFound:
        flash("Enrollment page not found.")
        # Redirect to the home page if the enrollment page is not found
        return redirect(url_for("home.home"))

# Route to handle saving a user's workshop enrollment
@enroll_bp.route("/createEnrollment", methods=["POST"])
def createEnrollment():
    try:
        # SAFETY CHECK: Prevent the KeyError if they somehow get here without logging in
        if "user_id" not in session:
            flash("Please log in first to enroll in workshops.")
            return redirect(url_for("user.login"))
            
        user_id = session["user_id"]
        timeslot_id = request.form["timeslot_id"]
        enroll.enroll_in_workshop(user_id, timeslot_id)
        flash("Successfully enrolled in the workshop.")
        # Redirect to the home page after successful enrollment
        return redirect(url_for("home.home"))

    except TemplateNotFound:
        flash("Enrollment page not found.")
        return redirect(url_for("home.home"))

# Route to display available timeslots for one specific workshop
@enroll_bp.route("/workshop/<int:workshop_id>/timeslots", methods=["GET"])
def workshop_timeslots(workshop_id):
    try:
        # Check if the user is logged in
        if "user_id" not in session:
            flash("Please log in first to view workshop timeslots.")
            return redirect(url_for("user.login"))
            
        user_id = session["user_id"]
        
        # Get the workshop details and the available timeslots
        workshop = enroll.get_workshop_details(workshop_id)
        if not workshop:
            flash("Workshop not found.")
            return redirect(url_for("home.home"))
            
        slots = enroll.get_timeslots_for_workshop(workshop_id, user_id)
        
        # Send the data to our new HTML template
        return render_template("workshop_timeslots.html", workshop=workshop, slots=slots)

    except TemplateNotFound:
        flash("Timeslots page not found.")
        return redirect(url_for("home.home"))
    