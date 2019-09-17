from src import db
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Ticket import Ticket


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_org = db.Column(db.Boolean, nullable=False, default=False)
    orders = db.relationship('Order', backref='user',
                             cascade="all,delete", lazy=True)
    org = db.relationship('Organizer', backref='user', uselist=False,
                          cascade="all,delete", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
