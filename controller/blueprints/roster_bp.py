#Purpose: render pages realted to workshop enrollment
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file


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

    
@roster_bp.route("/createCSV/<int:timeslot_id>/roster",methods=["GET"])
#reference documentation
#https://www.geeksforgeeks.org/python/how-to-create-csv-output-in-flask/
def create_csv(timeslot_id):
    myRoster = roster.get_roster(timeslot_id)
    
    #create headers
    csvString = "ID, First Name, Last Name, Permission Level\n"

    #append rows based on particpants
    for people in myRoster:
        csvString += f"{people[0]},{people[2]},{people[3]},{people[4]}\n"
    
    #dynamically name file based on timeslot
    filename = f"workshop_roster_timeslot_id_{timeslot_id}.csv"

    with open (filename,"w") as csv_file:
        csv_file.write(csvString)

    return send_file(filename, as_attachment=True, download_name=filename)




    