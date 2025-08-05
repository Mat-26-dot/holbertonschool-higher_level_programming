template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

Best regards,
Event Team
"""

attendees = [
    {"name": "Alice", "event_title": "Annual Gala", "event_date": "2025-12-01", "event_location": "Grand Ballroom"},
    {"name": "Bob", "event_title": "Annual Gala", "event_location": "Main Hall"}  # Missing event_date
]
