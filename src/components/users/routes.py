from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from src.models.User import Users
from src.components.users.forms import SignUp, LogInUser
from src import db, login

users_blueprint = Blueprint(
    'users', __name__, template_folder='../../templates/users')


@users_blueprint.route('/login', methods=['POST', 'GET'])
def login_u():
    form = LogInUser()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Login successful')
                return redirect(url_for('home'))
            else:
                flash('Incorrect email or password')
        for field_name, errors in form.errors.items():
            flash(errors[0])
    return render_template('log_in.html', form=form)


@users_blueprint.route('/new', methods=['POST', 'GET'])
def sign_up():
    form = SignUp()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                is_org=form.is_org.data
            )
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            if form.is_org.data:
                return redirect(url_for('organizers.register_organizer', id=new_user.id))
            flash('Successfully registered')
            return redirect(url_for('users.login_u'))
        else:
            for field, err in form.errors.items():
                flash(err[0], 'danger')
    return render_template('sign_up.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@users_blueprint.route('/purchase-history')
@login_required
def purchase_history():
    return render_template('history.html')


@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
