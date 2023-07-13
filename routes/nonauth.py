from fastapi import APIRouter,Response
from models.User import User
from services import userservices

routes=APIRouter(prefix="/nonauth")

@routes.get("/test")
def testserver():
    return {
        "status":True,
        "message":"non auth server success"
        }

@routes.post("/create")
def createUser(data:User):
    print("Inside create controller")
    return userservices.save_user(data)

@routes.get("/check")
def checkUser(email:str,password:str):
    print("Inside check controller")
    data={
        "email":email,
        "password":password
    }
    return userservices.check_user(data)