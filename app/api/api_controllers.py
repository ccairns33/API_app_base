# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import generate_password_hash, check_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.api.api_forms import LoginForm

# Import module models (i.e. User)
from app.api.api_models import User

# Define the blueprint: 'api', set its url prefix: app.url/api
mod_api = Blueprint('api', __name__, url_prefix='/api')

# url_name.com/api/supplemental
# Set the route and accepted methods
@mod_api.route('/supplemental', methods=['GET', 'POST'])
def signin_page():
    # TODO: Not necessary just filler info 

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('api.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("api/signin.html", form=form)

# url_name.com/api/supplemental/kpi-transit-data
@mod_api.route('/supplemental/kpi-transit-data', methods=['GET', 'POST'])
def api_kpi_transit_data_page():
    return "API | KPI transit data"