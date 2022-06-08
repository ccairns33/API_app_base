from random import choices
from flask import Flask
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField,SelectField,SubmitField, BooleanField

from wtforms.validators import DataRequired

# choices will the names of all the options. will be able to type in
# to the field and the company will pop up
class DataForm(FlaskForm):
    dropdown_list = ['Google', 'Lenovo', 'Dell']
    company = SelectField(label="Company Name", choices=dropdown_list, validators=[DataRequired()])
    submit = SubmitField("Send")
