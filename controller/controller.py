from flask import render_template, request, redirect, url_for
from model.model import model
from model import workshop

def manageRoutes(app):
    @app.route("/")
    def showHome():
        messages = model.getMessage()
        users = model.getUsers()
        return render_template("home.html", messages=messages, users=users)

    @app.route("/workshop")
    def showWorkshop():
        # Retrieve all data needed for the dropdown menus on the workshop page
        workshops = workshop.get_all_workshops()
        hosts = workshop.get_all_hosts()
        locations = workshop.get_all_locations()
        return render_template("workshop.html", workshops=workshops, hosts=hosts, locations=locations)

    @app.route("/createWorkshop", methods=["POST"])
    def createWorkshop():
        workshop_name = request.form["workshop_name"]
        hostID = request.form["hostID"]
        workshop.create_workshop(workshop_name, hostID)
        return redirect(url_for("showWorkshop"))

    @app.route("/createHost", methods=["POST"])
    def createHost():
        host_name = request.form["host_name"]
        workshop.create_host(host_name)
        return redirect(url_for("showWorkshop"))

    @app.route("/createLocation", methods=["POST"])
    def createLocation():
        location_name = request.form["location_name"]
        capacity = request.form["capacity"]
        workshop.create_location(location_name, capacity)
        return redirect(url_for("showWorkshop"))

    @app.route("/createTimeslot", methods=["POST"])
    def createTimeslot():
        workshop_id = request.form["workshop_id"]
        location_id = request.form["location_id"]
        session_datetime = request.form["session_datetime"]
        
        # HTML checkboxes send 'on' if checked, nothing if unchecked
        is_public = 1 if request.form.get("is_public") == "on" else 0
        
        workshop.create_timeslot(workshop_id, session_datetime, is_public, location_id)
        return redirect(url_for("showWorkshop"))

    @app.route("/createMessage", methods=["POST"])
    def createMessage():
        message = request.form["message"]
        model.createMessage()
        return redirect(url_for("showHome"))
        
    @app.route("/message")
    def messageForm():
       return render_template("message.html")