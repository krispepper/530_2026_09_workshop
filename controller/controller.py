from flask import render_template, request, redirect, url_for
from model.model import model

def manageRoutes(app):
    @app.route("/")
    def showHome():
        messages = model.getMessage()
        users = model.getUsers()
        return render_template("home.html",messages=messages,users=users)
        
        #return render_template("test.html",messages=messages)

    @app.route("/workshop")
    def showWorkshop():
        workshops = model.getWorkshops()
        hosts = model.getHosts()
        return render_template("workshop.html",workshops = workshops,hosts = hosts)

    @app.route("/createWorkshop", methods=["POST"])
    def createWorkshop():
        workshop_name = request.form["workshop_name"]
        hostID = request.form["hostID"]

        model.createWorkshop(workshop_name,hostID)
        return redirect(url_for("showWorkshop"))


    @app.route("/createMessage", methods=["POST"])
    def createMessage():
        message = request.form["message"]
        model.createMessage()
        
        return redirect(url_for("showHome"))
        
    @app.route("/message")
    def messageForm():
       return render_template("message.html")
