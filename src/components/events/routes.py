from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from src import db
from src.models.Event import Event
from src.models.TicketType import TicketType
from src.models.Ticket import Ticket
from src.models.Order import Order
from src.components.events.forms import NewEvent, NewTicketType
from datetime import datetime
# from src.components import organizers

events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='../../templates/events')


@events_blueprint.route('/upcoming')
def upcoming():
    events = Event.query.filter(Event.time > datetime.now()).all()
    return render_template('list.html', events=events)


@events_blueprint.route('/new', methods=['POST', 'GET'])
@login_required
def new_event():
    if current_user.is_org == True:
        form = NewEvent()
        if request.method == "POST":
            dt = (form.date.data).strftime("%d/%m/%Y")+' '+(
                form.time.data).strftime('%H:%M')
            if form.validate_on_submit():
                event = Event(name=form.name.data,
                              description=form.description.data,
                              time=datetime.strptime(dt, '%d/%m/%Y %H:%M'),
                              image_url=form.image_url.data,
                              venue_city=form.city.data,
                              venue_address=form.address.data,
                              organizer_id=current_user.org.id)
                db.session.add(event)
                db.session.commit()
                return redirect(url_for('events.new_ticket_type', id=event.id))
            else:
                for field, err in form.errors.items():
                    flash(err[0], 'danger')
        return render_template('new_event.html', form=form)
    else:
        flash('Only organizer account can create events', 'danger')
        return redirect(url_for('organizers.register_organizer'))


@events_blueprint.route('/ticket-types/<id>', methods=['POST', 'GET'])
@login_required
def new_ticket_type(id):
    if current_user.is_org == True:
        try:
            form = NewTicketType()
            if request.method == "POST":
                if form.validate_on_submit():
                    ticket_type = TicketType(name=form.name.data,
                                             price=form.price.data,
                                             quantity=form.quantity.data,
                                             event_id=id)

                    db.session.add(ticket_type)
                    db.session.commit()
                    flash('Added new ticket type')
                    return redirect(url_for('events.new_ticket_type', id=id))
                else:
                    for field, err in form.errors.items():
                        flash(err[0], 'danger')
            return render_template('new_ticket_type.html', form=form)
        except:
            flash('Event not exists')
            return redirect(url_for('home'))
    else:
        flash('Only organizer account can create events', 'danger')
        return redirect(url_for('organizers.register_organizer'))


@events_blueprint.route('view/<id>')
def view(id):
    event = Event.query.get(int(id))
    if event is not None:
        return render_template('event.html', event=event)
    flash('Event not exist!')
    return redirect(url_for('home'))


@events_blueprint.route('/purchase-ticket/<id>', methods=['POST', 'GET'])
@login_required
def purchase_ticket(id):
    event = Event.query.get(int(id))
    if event is not None:
        if request.method == 'POST':
            new_order = Order(user_id=current_user.id)
            total = 0
            for ticket_type in event.ticket_types:
                quantity = int(request.form[str(ticket_type.id)])
                if quantity <= ticket_type.get_available() and quantity <= 10 and quantity >= 0:
                    for i in range(quantity):
                        ticket = Ticket(ticket_type_id=ticket_type.id)
                        if ticket_type.is_available():
                            new_order.tickets.append(ticket)
                            total += ticket_type.price
                            db.session.add(ticket)
                            db.session.commit()
                        else:
                            flash(
                                f'Oops! Ticket {ticket_type.name} is sold out', 'danger')
                            break
                else:
                    flash('Quantity not valid', 'danger')
            new_order.total = total
            db.session.add(new_order)
            db.session.commit()
        return render_template('purchase.html', event=event)
    else:
        flash('Event not exist', 'danger')
    return redirect(url_for('home'))


@events_blueprint.route('/search', methods=['POST', 'GET'])
def search():
    key = request.form['search']
    print(key)
    events = Event.query.filter(Event.name.ilike(
        f'% {key}%') | Event.description.ilike(f'% {key}%')).all()
    print(events)
    return render_template('list.html', events=events)
