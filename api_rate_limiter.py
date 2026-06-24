#pip install slowapi

from fastapi import FastAPI,Request,status
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rateLimiterException(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "detail":"Too many Request"
        }
    )


@app.get("/user")
@limiter.limit("2/minute")
def isHealthyServer(request:Request,name:str):
    return {
        "status":f"Hello {name}....",
        "name": name
    }


@app.get("/user")
@limiter.limit("10/minute")
def isHealthyServer(request:Request):
    return {
        "status":"Hello Server",
        
    }