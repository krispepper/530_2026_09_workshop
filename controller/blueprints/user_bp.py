from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import user
from jinja2.exceptions import TemplateNotFound

user_bp = Blueprint('user', __name__, template_folder='templates')

 # Route to display the user registration form page
@user_bp.route("/register", methods=["GET"])
def showRegister():
    try:
        return render_template("register.html")
    except TemplateNotFound:
        flash("Registration page not found.")
        return redirect(url_for("home.home"))

# Route to handle registering a new user account
@user_bp.route("/createUser", methods=["POST"])
def createUser():
    try:
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        perms = request.form["perms"]
        email = request.form["email"]
        phone = request.form["phonenumber"]
        password = request.form["password"]
        user.create_user(first_name, last_name, email, password, phone, perms)
        flash("User account created successfully!")
        return redirect(url_for("user.login"))

    except TemplateNotFound:
        flash("Registration page not found.")
        return redirect(url_for("user.showRegister"))

# Route to handle user login authentication and session creation
@user_bp.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        logged_in_user = user.authenticate_user(email, password)
        if logged_in_user:
            session["user_id"] = logged_in_user[0]
            session["user_name"] = logged_in_user[1]
            session["perms"] = logged_in_user[4]
            return redirect(url_for("home.home"))
        else:
            flash("Invalid email or password. Please try again.")
    return render_template("login.html")

# Route to handle user logout and session termination
@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))

# Route to handle changing the user's password
@user_bp.route("/change-password", methods=["GET", "POST"])
def changePassword():
    
    if "user_id" not in session:
        return redirect(url_for("user.login"))

    if request.method == "POST":
        new_password = request.form["new_password"]
        user.update_password(session["user_id"], new_password)
        flash("Your password has been updated successfully!")
        return redirect(url_for("home.home"))
    return render_template("change_password.html")