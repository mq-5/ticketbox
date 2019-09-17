from src import db


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_type_id = db.Column(db.Integer, db.ForeignKey(
        'ticket_type.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
