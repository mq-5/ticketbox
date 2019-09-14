from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired, ValidationError
from wtforms.fields.html5 import DateField, TimeField


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
    time = TimeField('Time')
    submit = SubmitField('Create Event')


class NewTicketType(FlaskForm):
    name = StringField('Ticket type', validators=[
                       Length(max=120, message='Ticket type must not longer than 120 chars'), DataRequired()])
    price = IntegerField('Price', validators=[
                         DataRequired('Price is required')])
    quantity = IntegerField('Tickets Quantity', validators=[
                            DataRequired('Quantity is required')])

    def validate_price(self, field):
        if field.data < 0:
            raise ValidationError('Price must not be negative')

    def validate_quantity(self, field):
        if field.data < 0:
            raise ValidationError('Quantity must not be negative')
