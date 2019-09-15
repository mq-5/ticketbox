from src import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String)
    venue_city = db.Column(db.String(50), nullable=False)
    venue_address = db.Column(db.String, nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey(
        'organizers.id'))
    ticket_types = db.relationship(
        'TicketType', backref='event', lazy=True, cascade="all,delete")
