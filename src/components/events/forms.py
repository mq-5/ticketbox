from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import Length, DataRequired, ValidationError
from wtforms.fields.html5 import DateField, TimeField
from babel.numbers import format_number, format_decimal
from datetime import datetime


class NewEvent(FlaskForm):
    name = StringField('Event Name', validators=[Length(
        max=128, message='Event name should not be longer than 128 chars'), DataRequired('Event name is required')])
    description = StringField('Description', validators=[
                              DataRequired('Description is required')])
    image_url = StringField('Image URL')
    address = StringField('Address', validators=[
                          DataRequired('Event address is required')])
    city = StringField('City', validators=[DataRequired(
        'Event city is required'), Length(max=50)])
    date = DateField('Date:', validators=[
        DataRequired('Event date is required')])
    time = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Create Event')

    def validate_date(self, field):
        if field.data <= datetime.now().date():
            raise ValidationError('Event must be from tomorrow')


class NewTicketType(FlaskForm):
    name = StringField('Ticket type', validators=[
                       Length(max=120, message='Ticket type must not longer than 120 chars'), DataRequired()])
    price = DecimalField('Price', validators=[
                         DataRequired('Price is required')], places=0, rounding='ROUND_DOWN')
    quantity = IntegerField('Tickets Quantity', validators=[
                            DataRequired('Quantity is required')])
    submit = SubmitField('Add')

    def validate_price(self, field):
        if field.data < 0:
            raise ValidationError('Price must not be negative')

    def validate_quantity(self, field):
        if field.data < 0:
            raise ValidationError('Quantity must not be negative')
