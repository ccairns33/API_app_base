# Blueprint instantiation for api package
from flask import Blueprint
mod_api = Blueprint('api', __name__, url_prefix='/api')

# from app.api import api_controllers