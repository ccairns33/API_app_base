from flask import Flask, render_template

#Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object 
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

# sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return render_template("404.html"), 404

# import a module / component using its blueprint handler variable (mod_auth)
from app.api.api_controllers import mod_api as api_module
from app.gnmc.gnmc_controllers import mod_gnmc as gnmc_module


# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(gnmc_module)

# Build the database
# This will create the database file using SQLAlchemy
db.create_all()