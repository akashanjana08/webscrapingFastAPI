from fastapi import FastAPI,HTTPException,status
app = FastAPI();




@app.get("/user",status_code=status.HTTP_200_OK)
def getUserData(name:str):
    if name != 'akash' :
       raise HTTPException(
           status_code=404,
           detail=f'Input user {name} not  found'
       )

    return {"message":"Success"}