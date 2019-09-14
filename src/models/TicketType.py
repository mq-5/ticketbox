from src import db


class TicketType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False, default=0)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
