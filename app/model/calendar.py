from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


#TODO: Implement Reminder class here

class Reminder:
    EMAIL = "email"
    SYSTEM = "system"

    def __init__(self, date_time: datetime):
        self.date_time: datetime = date_time
        self.type: str = self.EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {type}"





#TODO: Implement Event class here


#TODO: Implement Day class here


#TODO: Implement Calendar class here
