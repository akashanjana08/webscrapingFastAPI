from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Address(BaseModel):
     house:str
     city:str
     country:str

class User(BaseModel):
      name:str
      id:int
      address: Address


@app.get("/")
def home():
    return {'name':'Home'}

@app.get("/user/{name}")
def get_username(name: int):
    return {
        "userName": name
    }

@app.get("/pagination")
def get_pageBumber(page: int= 10):
    return {
        "pageNumber":page
    }


@app.post("/register")
def user_registration(reg:User):
    return {
        "message": "Registration Successfully",
        "user": reg
    }
