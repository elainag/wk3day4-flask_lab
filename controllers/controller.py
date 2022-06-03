from flask import render_template, request
from models.events_list import *
from models.event import *
from app import app


@app.route("/all_events")
def index():
    return render_template("index.html", title="Events_Home", all_events=all_events)


@app.route("/all_events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event_name"]
    number_guests = request.form["num_guests"]
    location = request.form["room_location"]
    description = request.form["description"]
    new_event = Event(event_date, event_name, number_guests, location, description)
    add_new_event(new_event)
    return render_template("index.html", title="New Event", all_events=all_events)


@app.route("/recurring")
def all_recurring():
    return render_template(
        "recurring.html", title="Recuring Events", all_events=all_recurring
    )
