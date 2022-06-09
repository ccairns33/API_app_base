# Blueprint instantiation for gnmc package
from flask import Blueprint
mod_gnmc = Blueprint('gnmc',__name__, url_prefix='/gnmc')

# from app.gnmc import gnmc_controllers