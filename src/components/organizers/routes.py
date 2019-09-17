from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, current_user, logout_user
from src.models.Organizer import Organizer
from src.models.User import Users
from src.components.organizers.forms import RegisterOrganizer
from src import db, login

organizers_blueprint = Blueprint(
    'organizers', __name__, template_folder='../../templates/organizers')


@organizers_blueprint.route('/register/<id>', methods=['POST', 'GET'])
def register_organizer(id):
    user = Users.query.get(int(id))
    if user and user.org:
        flash('You can create only one org!', 'danger')
        return redirect(url_for('home'))
    if user and user.is_org:
        form = RegisterOrganizer()
        if request.method == 'POST':
            if form.validate_on_submit():
                new_organizer = Organizer(
                    name=form.company.data,
                    description=form.description.data,
                    image_url=form.image_url.data,
                    user_id=id
                )
                db.session.add(new_organizer)
                db.session.commit()
                flash('Successfully registered!')
                return redirect(url_for('home'))
            else:
                for field, err in form.errors.items():
                    flash(err[0], 'danger')
        return render_template('register.html', form=form)
    else:
        flash('Not allowed for this user', 'danger')
        return redirect(url_for('home'))


@organizers_blueprint.route('/profile/<id>')
def profile(id):
    org = Organizer.query.get(id)
    return render_template('profile_org.html', org=org)
