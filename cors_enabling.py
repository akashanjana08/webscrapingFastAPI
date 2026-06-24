from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins =[
    "http://my-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credential=True,
    allow_methods= ["*"], #put,post,get,delete   
    allow_headers = ["*"]
)

@app.get("/")
def getData():
    return {
        "data":"Hello World"
    }