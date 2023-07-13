from pydantic import BaseModel,validator

class User(BaseModel):
    username:str
    email:str
    password:str
    
    

