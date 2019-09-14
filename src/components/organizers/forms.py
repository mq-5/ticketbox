from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from src.models.Organizer import Organizer


class RegisterOrganizer(FlaskForm):
    company = StringField('Organization Name', validators=[Length(
        max=128, message='Name should not be longer than 128 chars'), DataRequired('Company name is required')])
    description = TextAreaField('Description')
    image_url = StringField('Image')
    submit = SubmitField('Register')
