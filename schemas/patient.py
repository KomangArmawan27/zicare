from enum import Enum as PydanticEnum
from pydantic import BaseModel

class GenderEnum(str, PydanticEnum):
    p = "p"
    l = "l"


class Patient(BaseModel):
    name: str
    gender: GenderEnum
    addres: str