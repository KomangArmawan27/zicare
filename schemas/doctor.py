from enum import Enum as PydanticEnum
from pydantic import BaseModel

class GenderEnum(str, PydanticEnum):
    p = "p"
    l = "l"


class Doctor(BaseModel):
    name: str
    gender: GenderEnum
    addres: str
    specialty: str