from fastapi import FastAPI,Depends
import time
from common.webscraping import fetchNews

app = FastAPI()

url = "https://"

#cache storage
cache_data = []
last_fetch = 0



@app.get("/headlines")
def fetchNewsAPI():
    global cache_data,last_fetch
    start = time.time()
    print(start)
    if time.time() - last_fetch > 60 :
        #fetch api
        print("Fetching data.....")
        cache_data = fetchNews()
        last_fetch = time.time()
    else:
        print("cache Data")

    return {
        "headlines": cache_data
    }


