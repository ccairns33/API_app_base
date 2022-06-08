from flask import Flask, render_template
from app.config import Config
#Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy



# Define the database object which is imported by modules and controllers
db = SQLAlchemy()

# # sample HTTP error handling
# @app.errorhandler(404)
# def not_found():
#     return render_template("404.html"), 404


# Build the database
# This will create the database file using SQLAlchemy


# Application Factory
def create_app(config_class=Config):
    # Define the WSGI application object 
    app = Flask(__name__)

    # Configurations
    app.config.from_object(Config)
    
    db.init_app(app)

    # import a module / component using its blueprint handler variable (mod_auth)
    from app.api.api_controllers import mod_api as api_module
    from app.gnmc.gnmc_controllers import mod_gnmc as gnmc_module


    # Register blueprint(s)
    app.register_blueprint(api_module)
    app.register_blueprint(gnmc_module)

    with app.app_context():
        db.create_all()

    return app