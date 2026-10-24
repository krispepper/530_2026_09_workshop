#Purpose: render pages realted to workshop enrollment
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from jinja2.exceptions import TemplateNotFound
from model import enroll, roster
import csv

roster_bp = Blueprint('roster', __name__, template_folder='templates')
@roster_bp.route("/timeslot/<int:timeslot_id>/roster", methods=["GET"])
def show_roster(timeslot_id):
    try:
        # Get the workshop details and the available timeslots
        timeslotRoster = roster.get_roster(timeslot_id)
        
        # Send the data to our new HTML template
        return render_template("roster.html", timeslotRoster = timeslotRoster)

    except TemplateNotFound:
        flash("Timeslots page not found.")
        return redirect(url_for("home.home"))

    
# @roster_bp.route("/createCSV")
#     def create_csv():



    