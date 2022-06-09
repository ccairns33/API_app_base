from flask import Flask, request, render_template
from app.config import Config
#Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse




# Define the database object which is imported by modules and controllers
db = SQLAlchemy()
# Define the api object
api = Api()

# # sample HTTP error handling
def register_error_handlers(app):
    # 404 Page Not Found
    @app.errorhandler(404)
    def not_found():
        return render_template("404.html"), 404


# Build the database
# This will create the database file using SQLAlchemy

names = {
        "carla": {"age":22, "gender": "female"},
        "bill": {"age": 47, "gender": "male"}
        }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    def post(self, name):
        return {"data": " Posted"}
         
api.add_resource(HelloWorld, "/helloworld/<string:name>")



# Application Factory
def create_app(config_class=Config):
    # Define the WSGI application object 
    app = Flask(__name__)

    

    # Configurations
    app.config.from_object(Config)
    
    api.init_app(app)
    db.init_app(app)

    # import a module / component using its blueprint handler variable
    from app.api.api_controllers import mod_api as api_module
    from app.gnmc.gnmc_controllers import mod_gnmc as gnmc_module


    # Register blueprint(s)
    app.register_blueprint(api_module)
    app.register_blueprint(gnmc_module)

    # Register Errors
    # register_error_handlers(app)

    # without app.app_context app throw an error. must push an application context for sql alchemy
    with app.app_context():
        db.create_all()

    return app