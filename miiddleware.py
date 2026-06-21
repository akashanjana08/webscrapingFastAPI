from fastapi import FastAPI, Request,Header,Depends
from fastapi.responses import JSONResponse
app = FastAPI();


def verifyToken(token:str = Header(None)):
    return token == "krishna"


@app.middleware("http")
async def checkAuthentication(request:Request,call_next):
    print(f"Path: {request.url} {request.headers}")
    token = request.headers.get("token")
    if not verifyToken(token):
      return JSONResponse(
            status_code=401,
            content={
                "message": "Unauthorized Token"
            }
        )
    response =await call_next(request)
    print("Response sent")
    return response


@app.get("/home")
def home():
    return {
        "Message" : 'Welcome User'
    }

@app.get("/contact")
def contact():
    return {
        "Message" : 'Welcome Contact User'
    }