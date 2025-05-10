from pydantic import BaseModel, Field
from datetime import date, time
from typing import Literal

class Reminder(BaseModel):
    userid: str
    date: date
    time: time
    message: str
    reminder_type: Literal['sms', 'email']