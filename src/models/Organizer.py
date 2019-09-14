from src import db


class Organizer(db.Model):
    __tablename__ = 'organizers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    events = db.relationship('Event', backref='organizer',
                             lazy='dynamic', cascade="all,delete")
