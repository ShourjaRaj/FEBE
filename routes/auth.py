from fastapi import APIRouter,Request
from utility.hashing import verify1
from models.Diabetes import Diabetes
from models.Heart import Heart
from services.mlservices import diabetes,heart

routes=APIRouter(prefix="/auth")

@routes.get("/test")
def testserver(req:Request):
    headers=dict(req.headers)
    return {
        "status":True,
        "message":"auth server success",
        "data":verify1(headers["authorization"].split(" ")[1])
        }


@routes.post("/diabetes")
def predict_diabetes(data:Diabetes):
    return diabetes(data)


@routes.post("/heart")
def predict_diabetes(data:Heart):
    return heart(data)