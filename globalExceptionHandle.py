from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse
app=FastAPI()


class UserNotFoundException(Exception):
    def __init__(self, name):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception(request:Request,exec:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"Error",
            "message":f'User {exec.name} not found'
        }
    )

@app.get("/user")
def getUser(name:str):
    if name == 'rupak':
        raise UserNotFoundException(name)

    return {"msg":"Success"}