from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    id:int
    name: str
    age:int

userList = []

@app.get("/user")
def getAllUserList():
    return {"userList":userList}


@app.post("/user")
def addUser(user: User):
    userList.append(user)
    return {"message": "User added Successfully", "user": user}


@app.put("/user")
def updateUser(user: User):
    for index,u in enumerate(userList):
        if user.id == u.id :
            userList[index] = user

    return {"message": "User Update Successfully"}


@app.delete("/user")
def deleteUser(userId: int):
    for index,u in enumerate(userList):
        if userId == u.id :
            userList.pop(index)

    return {"message": "User Deleted Successfully"}
        