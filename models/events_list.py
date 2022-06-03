from models.event import *

event1 = Event("05-05-2022", "event1", 10, "third_floor", "birthday_party", True)
event2 = Event("15-06-2022", "event2", 50, "ground_floor", "corporate_event", False)
event3 = Event("25-05-2022", "event3", 25, "s", "retirement_party", False)
all_events = [event1, event2, event3]


def add_new_event(event):
    all_events.append(event)


def recurring_events(event):
    recurring = []
    for event in all_events:
        if event.recurring == True:
            recurring.append(event)
            return recurring
