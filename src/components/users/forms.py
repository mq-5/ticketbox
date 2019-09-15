from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from src.models.User import Users


class SignUp(FlaskForm):
    first_name = StringField('First Name:', validators=[Length(
        max=80, message='First name should not be longer than 80 chars'), DataRequired('First name is required')])
    last_name = StringField('Last Name:', validators=[Length(
        max=80, message='Last name should not be longer than 80 chars'), DataRequired('Last name is required')])
    email = StringField('Email', validators=[
                        DataRequired('Email is required')])
    password = PasswordField('Password', validators=[
                             DataRequired('Please enter password')])
    password_cf = PasswordField("Re-enter Password", validators=[
        DataRequired(), EqualTo('password', message='Passwords not matching')])
    is_org = BooleanField('Sign up for an organization')
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email has been registered')


class LogInUser(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired('Email is required')])
    password = PasswordField('Password', validators=[
                             DataRequired('Please enter password')])
    submit = SubmitField('Log In')
