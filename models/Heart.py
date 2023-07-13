from pydantic import BaseModel
from typing import Literal


class Heart(BaseModel):
    age:int
    gender:Literal[0,1]
    cp:int
    trestbps:int
    chol:int
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:float
    slope:int
    ca:int
    thal:int