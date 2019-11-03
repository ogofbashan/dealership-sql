from app import app, db
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class NameForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Search')


class MaintenanceForm(FlaskForm):
    payment_id = IntegerField('PAYMENT ID', validators=[DataRequired()])
    staff_id = IntegerField('STAFF ID', validators=[DataRequired()])
    date_started = DateTimeField('Start Date' ,validators=[DataRequired()])
    date_finished = DateTimeField('Completion Date', validators=[DataRequired()])
    description= StringField('What did you do?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email= StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
