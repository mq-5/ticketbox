from src import db
# from src.models import Users


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_type_id = db.Column(db.Integer, db.ForeignKey(
        'ticket_type.id'), nullable=False)
