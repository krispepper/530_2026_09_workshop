from flask import render_template, request, redirect, url_for, session, flash
from model.model import model
from model import workshop
from model import user 
from model import enroll

def manageRoutes(app):
    @app.route("/")
    def showHome():
        messages = model.getMessage()
        users = user.get_all_users() 
        return render_template("home.html", messages=messages, users=users)

    @app.route("/workshop")
    def showWorkshop():
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
        
        is_public = 1 if request.form.get("is_public") == "on" else 0
        
        workshop.create_timeslot(workshop_id, session_datetime, is_public, location_id)
        return redirect(url_for("showWorkshop"))

    @app.route("/createMessage", methods=["POST"])
    def createMessage():
        message = request.form["message"]
        model.createMessage(message)
        return redirect(url_for("showHome"))
        
    @app.route("/message")
    def messageForm():
       return render_template("message.html")

    @app.route("/register", methods=["GET"])
    def showRegister():
        return render_template("register.html")

    @app.route("/createUser", methods=["POST"])
    def createUser():
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        perms = request.form["perms"]
        email = request.form["email"]
        phone = request.form["phonenumber"]
        password = request.form["password"] # Added password capture
        
        user.create_user(first_name, last_name, perms, email, phone, password)
        
        return redirect(url_for("login"))

    @app.route("/enroll", methods=["GET"])
    def showEnroll():
        
        if "user_id" not in session:
            flash("Please log in first to enroll in workshops.")
            return redirect(url_for("login"))
            
        user_id = session["user_id"]

        slots = enroll.get_available_timeslots(user_id)
        
        return render_template("enroll.html", slots=slots)

    @app.route("/createEnrollment", methods=["POST"])
    def createEnrollment():
        user_id = request.form["user_id"]
        timeslot_id = request.form["timeslot_id"]
        
        enroll.enroll_in_workshop(user_id, timeslot_id)
        
        return redirect(url_for("showHome"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            
            logged_in_user = user.authenticate_user(email, password)
            
            if logged_in_user:
                session["user_id"] = logged_in_user["id"]
                session["user_name"] = logged_in_user["firstName"]
                session["perms"] = logged_in_user["perms"]
                return redirect(url_for("showHome"))
            else:
                flash("Invalid email or password. Please try again.")
                
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

    @app.route("/change-password", methods=["GET", "POST"])
    def changePassword():
        # Check if user is logged in first using the session
        if "user_id" not in session:
            return redirect(url_for("login"))
            
        if request.method == "POST":
            new_password = request.form["new_password"]
            user.update_password(session["user_id"], new_password)
            flash("Your password has been updated successfully!")
            return redirect(url_for("showHome"))
            
        return render_template("change_password.html")