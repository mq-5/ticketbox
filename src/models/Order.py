from src import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tickets = db.relationship(
        'Ticket', backref='order', lazy=True, cascade='all,delete')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
