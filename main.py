from fastapi import FastAPI
from routes import nonauth,auth
from middleware.checktoken import Middleware
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins = ["*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(Middleware)

@app.get("/")
def testserver():
    return {
        "status":True,
        "message":"Root server success"
        }

app.include_router(nonauth.routes)
app.include_router(auth.routes)