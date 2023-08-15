from datetime import date, time, datetime
from pydantic import BaseModel


class Doctor_slot(BaseModel):
    doctor_id: int
    startTime: str
    endTime: str
    startDate: date
    endDate: date
    location: str

