
## User Stories

The following **required** functionality is complete:

#### Events

* [x] Users can see a list of upcoming events. Past events should not be shown.
    * **HINT**: Good candidate for a test. You can write test first --> fail --> fast similar to demo
    * Suggestions:
        * Implement `/upcoming` route test to go to 'events#index'
        * Implement `Event.upcoming` class method (with a test)
        * Implement `EventsController#index` action test
* [ ] Users can search for events from the homepage.
* [x] Users can click on an event to see details about the event.
* [ ] Users can click on "Book Now" to go to a page to purchase tickets.

#### Tickets

* [x] Each event can have multiple types of tickets, each with a different `price` and `max_quantity`.
* [ ] Users can buy tickets to an event, choose the types of tickets, and the quantity of tickets.
* [x] Users cannot buy more tickets than the quantity available.
* [ ] Users can only buy up to 10 of a ticket type at a time. Show a nice flash message.

#### Users

* [x] User can sign up by providing their email, password, and name.
* [x] User can login using an email and password.
* [x] Users can create events.
* [ ] Users must click "publish event" before an event becomes viewable to other users.
    * **HINT**: use `published_at:datetime` and `Event.published` scope (class method)
    * Suggestions:
        * See [Add More RESTful Actions](http://guides.rubyonrails.org/routing.html#adding-more-restful-actions) to add a `publish` POST action (member type)
        * Write a test to make sure only an event creator can publish an event
* [x] Users can create ticket types for that event.
    * **HINT**: make sure you understand what a ticket type is. Ask if not clear.
* [x] Users can create venues.
* [ ] An event must have at least one `ticket_type` defined before it can be published.
    * **HINT**: add `Event#have_enough_ticket_types?` (and test it)
* [ ] User can see a list of events he or she has created.
    * Suggestions
        * You can use `/events/mine` [collection routes](http://guides.rubyonrails.org/routing.html#adding-more-restful-actions)
* [ ] Users can edit their event after creation. But only the user who created the event can edit the event.
    * **HINT**: use a `before_action :cx`