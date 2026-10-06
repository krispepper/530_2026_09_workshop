from flask import Blueprint, render_template, redirect, abort
from jinja2.exceptions import TemplateNotFound


admin_bp = Blueprint('admin', __name__, template_folder='templates')
@admin_bp.route("/admin", methods=["GET"])
def showRegister():
    try:
        return render_template("admin.html")
    except TemplateNotFound:
        flash("Registration page not found.")
        return redirect(url_for("home.home"))