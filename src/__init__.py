from datetime import datetime
import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT'],
}

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Admin
app.config['FLASK_ADMIN_SWATCH'] = 'Flatly'
admin = Admin(app, name='Ticketbox', template_mode='bootstrap3')


db = SQLAlchemy(app)
Migrate(app, db)

login = LoginManager(app)


from src.components.events.routes import events_blueprint  # noqa
from src.components.organizers.routes import organizers_blueprint  # noqa
from src.components.users.routes import users_blueprint  # noqa
app.register_blueprint(events_blueprint, url_prefix='/events')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(organizers_blueprint, url_prefix='/organizers')


from src.models.User import Users  # noqa
from src.models.Event import Event  # noqa
from src.models.Organizer import Organizer  # noqa
from src.models.TicketType import TicketType  # noqa
from src.models.Ticket import Ticket  # noqa


login.login_view = 'users.login_u'

admin.add_view(ModelView(Users, db.session, endpoint='user'))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Organizer, db.session))
admin.add_view(ModelView(TicketType, db.session))
admin.add_view(ModelView(Ticket, db.session))


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/')
def home():
    events = Event.query.filter(Event.time > datetime.now()).all()
    return render_template('list.html', events=events)


@app.route('/cur')
def cur():
    return f'CURRENT {current_user.email}' if current_user.is_active else 'None'
