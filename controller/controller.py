#Purpose: manage bluprints into a unified routing system. I pass this to app.py to serve users all the pages they need in our app.
from controller.blueprints.home_bp import home_bp
from controller.blueprints.message_bp import message_bp
from controller.blueprints.workshop_bp import workshop_bp
from controller.blueprints.user_bp import user_bp
from controller.blueprints.enroll_bp import enroll_bp
from controller.blueprints.admin_bp import admin_bp
from controller.blueprints.browse_bp import browse_bp
from controller.blueprints.inbox_bp import inbox_bp
from controller.blueprints.roster_bp import roster_bp
from flask import session

#context processor to inject session into base template navbar
#this lets me get user info in navbar without having to do a session.get eachtime
def injectUser():
    if "user_id" not in session:
        return {"loggedIn":None}
    
    else:
        return {"loggedIn": {
            "id": session.get("user_id"),
            "name": session.get("user_name"),
            "perms": session.get("perms")
        }}
             
#registers routes from the blueprints folder
def manageRoutes(app):
    app.context_processor(injectUser)
    app.register_blueprint(home_bp)
    app.register_blueprint(inbox_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(browse_bp)
    app.register_blueprint(roster_bp)
    #app.register_blueprint(message_bp)
    app.register_blueprint(workshop_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(enroll_bp)
    