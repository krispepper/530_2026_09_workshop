from flask import Blueprint, render_template, redirect, request, url_for
from model import workshop
from jinja2.exceptions import TemplateNotFound

workshop_bp = Blueprint('workshop', __name__, template_folder='templates')

# Route to display the workshop management page with existing workshops, hosts, and locations
@workshop_bp.route("/workshop")
def showWorkshop():
    try:
        workshops = workshop.get_all_workshops()
        hosts = workshop.get_all_hosts()
        locations = workshop.get_all_locations()
        return render_template("workshop.html", workshops=workshops, hosts=hosts, locations=locations)
    except TemplateNotFound:
        flash("Workshop management page not found.")
        return redirect(url_for("home.home"))
    

# Route to handle creating a new workshop from form data
@workshop_bp.route("/createWorkshop", methods=["POST"])
def createWorkshop():

    try:
        workshop_name = request.form["workshop_name"]
        hostID = request.form["hostID"]
        workshop.create_workshop(workshop_name, hostID)
        return redirect(url_for("workshop.showWorkshop"))

    except TemplateNotFound:
        flash("Workshop creation page not found.")
        return redirect(url_for("workshop.showWorkshop"))


# Route to handle creating a new host
@workshop_bp.route("/createHost", methods=["POST"])

def createHost():
    try:
        host_name = request.form["host_name"]
        workshop.create_host(host_name)
        return redirect(url_for("workshop.showWorkshop"))

    except TemplateNotFound:
        flash("Host creation page not found.")
        return redirect(url_for("workshop.showWorkshop"))


# Route to handle creating a new room location and capacity
@workshop_bp.route("/createLocation", methods=["POST"])
def createLocation():

    try:
        location_name = request.form["location_name"]
        capacity = request.form["capacity"]
        workshop.create_location(location_name, capacity)
        return redirect(url_for("workshop.showWorkshop"))

    except TemplateNotFound:
        flash("Location creation page not found.")
        return redirect(url_for("workshop.showWorkshop"))

# Route to handle scheduling a new workshop time slot and visibility
@workshop_bp.route("/createTimeslot", methods=["POST"])
def createTimeslot():
    try:
        workshop_id = request.form["workshop_id"]
        location_id = request.form["location_id"]
        session_datetime = request.form["session_datetime"]
        is_public = 1 if request.form.get("is_public") == "on" else 0
        workshop.create_timeslot(workshop_id, session_datetime, is_public, location_id)
        return redirect(url_for("workshop.showWorkshop"))
    except TemplateNotFound:
        flash("Timeslot creation page not found.")
        return redirect(url_for("workshop.showWorkshop"))