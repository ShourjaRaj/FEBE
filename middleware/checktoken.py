from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse
from utility.messages import (
    getErrorMessage
)
from utility.hashing import verify1

class Middleware(BaseHTTPMiddleware):
    async def dispatch(self,req:Request,call_next):
        # print("The path:",req.url.path)
        path=req.url.path
        print("The path:",path)
        if("nonauth" in path):
            # print(231)
            return await call_next(req)
        try:
            headers=dict(req.headers)
            print(headers)
            if("authorization" in headers and verify1(headers["authorization"].split(" ")[1])):
                # print(231)
                return await call_next(req)
            else:
                return JSONResponse(getErrorMessage("Auth key not present"),status_code=403)
        except Exception as e:
            print(e,type(e))
            if(str(e)=="Signature has expired"):
                return JSONResponse(getErrorMessage(str(e)),status_code=401)
            return JSONResponse(getErrorMessage("123"),status_code=500)