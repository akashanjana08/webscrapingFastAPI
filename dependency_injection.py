from fastapi import FastAPI, Depends,Header,HTTPException,status
app = FastAPI();


def verify_auth(token:str = Header(None)):
    if token == 'krishna':
        return {
            "message":"Authentication Successs" 
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User Unauthrized"
    ) 


@app.get("/auth")
def auth(isAuth:str = Depends(verify_auth)):
    return isAuth
    
