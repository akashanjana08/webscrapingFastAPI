from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI();

class User(BaseModel):
    name:str
    mobile:str
    password:str

class UserResponse(BaseModel):
    name:str
    mobile:str


@app.post("/user",response_model=UserResponse)
def addUser(user:User):
    return user
