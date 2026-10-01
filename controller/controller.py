#Purpose: manage bluprints into a unified routing system. I pass this to app.py to serve users all the pages they need in our app.
from controller.blueprints.home_bp import home_bp
from controller.blueprints.message_bp import message_bp
from controller.blueprints.workshop_bp import workshop_bp
from controller.blueprints.user_bp import user_bp
from controller.blueprints.enroll_bp import enroll_bp

#registers routes from the blueprints folder
def manageRoutes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(workshop_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(enroll_bp)
    