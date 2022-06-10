# Import flask dependencies
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    current_app,
)

# Import password / encryption helper tools
from werkzeug.security import generate_password_hash, check_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.gnmc.gnmc_forms import DataForm

# import blueprint from the init.py file
from app.gnmc import mod_gnmc

# Import module models (i.e. User)
# from app.api.gnmc_models import Data

# Define the blueprint: 'gnmc', set its url prefix: app.url/gnmc
# mod_gnmc = Blueprint('gnmc',__name__, url_prefix='/gnmc')
# url_name.com/gnmc/supplemental
# Set the route and accepted methods


# url_name.com/gnmc/supplemental/kpi-transit-data
@mod_gnmc.route("/supplemental/kpi-transit-data", methods=["GET", "POST"])
def gnmc_kpi_transit_data_page():
    form = DataForm(request.form)
    # if form.validate_on_submit():
    # user = User.query.filter_by(email=form.email.data).first()
    # if user and check_password_hash(user.password, form.password.data):
    #     session['user_id'] = user.id
    #     flash('Welcome %s' % user.name)
    #     return redirect(url_for('api.home'))
    # flash('Wrong email or password', 'error-message')
    return render_template("gnmc/kpi-data-input.html", form=form)


@mod_gnmc.route("/supplemental", methods=["GET", "POST"])
def gnmc_supplemental_page():
    return "gnmc supplemental page"
