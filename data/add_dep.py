from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from flask import redirect
from datetime import datetime


class DepForm(FlaskForm):
    title = StringField('Title of the Department', validators=[DataRequired()])
    chief = IntegerField('Chief of the Department', validators=[DataRequired()])
    members = StringField('Involved colonists id', validators=[DataRequired()])
    email = EmailField('Email of the Department', validators=[DataRequired()])
    submit = SubmitField('Submit')
