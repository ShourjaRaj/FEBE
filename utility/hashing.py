from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime,timedelta
from starlette.responses import JSONResponse
from utility.messages import getErrorMessage

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(plainp):
    return pwd_context.hash(plainp)


def verify(plainp,dbp):
    return pwd_context.verify(plainp, dbp)


def hash1(data:dict):
    data["exp"]=datetime.utcnow()+timedelta(hours=3)
    data["iat"]=datetime.utcnow()
    return jwt.encode(data,os.getenv("JWT_KEY"),algorithm="HS256")

def verify1(token):
    # print(type(token))
    return jwt.decode(token,os.getenv("JWT_KEY"),algorithms=["HS256"])
# print(verify1("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3QyQGdtYWlsLmNvbSIsImlkIjoiNjQ1NzI5ZjE4MzlhZTNmMTQ2Nzg3YTlhIn0.GSb6IqaWC3vdh1ttZFiSQ5CJG24eKfAyhHwUyT6NoJ0"))