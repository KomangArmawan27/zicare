from datetime import date
from pydantic import BaseModel, Field

class Reservation(BaseModel):
    doctor_id: int
    patient_id: int
    encounter_date: date
    encounter_time: str = Field(..., example="16.00")
