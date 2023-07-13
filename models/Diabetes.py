from pydantic import BaseModel
from typing import Literal


class Diabetes(BaseModel):
    gender:Literal[0,1]
    age:int
    hypertension:Literal[0,1]
    heart_disease:Literal[0,1]
    smoking:Literal[0,1]
    bmi:float
    HbA1c_level:float
    blood_glucose_level:int