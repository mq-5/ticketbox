
import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, logout_user, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT'],
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login = LoginManager(app)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logged out'


from src.components.events.routes import events_blueprint  # noqa
from src.components.organizers.routes import organizers_blueprint  # noqa
from src.components.users.routes import users_blueprint  # noqa
app.register_blueprint(events_blueprint, url_prefix='/events')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(organizers_blueprint, url_prefix='/organizers')


from src.models.Organizer import Organizer  # noqa
from src.models.User import Users  # noqa
@login.user_loader
def load_user(id, role):
    if role == 'org':
        return Organizer.query.get(int(id))
    return Users.query.get(int(id))


@app.route('/cur')
def cur():
    return f'CURRENT {current_user.email}'
