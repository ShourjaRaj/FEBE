from config.dbconnection import user as dbuser
from schemas.user import user
from utility.hashing import (
    verify,hash,hash1,verify1
)
from utility.messages import (
    getErrorMessage,getSuccessMessage
)
from starlette.responses import JSONResponse

def save_user(data):
    try:
        email=data.email
        if(dbuser.find_one({"email":email})):
            return JSONResponse(getErrorMessage("User with this email id already exist"),status_code=400)
        data.password=hash(data.password)
        dbuser.insert_one(dict(data))
        return JSONResponse(getSuccessMessage("User created successfully"),status_code=201)
    except Exception as e:
        print("services save",e)
        return JSONResponse(getErrorMessage("Something went wrong"),status_code=500)




def check_user(data):
    try:
        userData=dbuser.find_one({"email":data["email"]})
        if(userData is None):
            return JSONResponse(getErrorMessage("User does not exist"),status_code=400)
        userData=user(userData)
        if(not verify(data["password"],userData["password"])):
            return JSONResponse(getErrorMessage("Wrong password"),status_code=403)
        return JSONResponse({
            "status":True,
            "auth_key":hash1({
            "email":userData["email"],
            "id":userData["id"]
            })
        })
    except Exception as e:
        print(e)
        return JSONResponse(getErrorMessage("Something went wrong"),status_code=500)
    
