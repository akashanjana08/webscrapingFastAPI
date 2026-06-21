from fastapi import FastAPI,HTTPException,Depends
import requests
from bs4 import BeautifulSoup

url = "https://www.aajtak.in/"
async def updatedHeadlines():
    

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    # Find the sm-thumb-listing div
    thumb_listing = soup.find("div", class_="sm-thumb-listing")

    # Extract titles from li tags
    if thumb_listing:
        li_tags = thumb_listing.find_all("li", attrs={"data-tb-region-item": True})
        titles = []
        for li in li_tags:
            a_tag = li.find("a")
            if a_tag and a_tag.get("title"):
                titles.append(a_tag.get("title"))
        
        # print("Titles from li tags:")
        # for title in titles:
        #     print(f"- {title}")
        return titles
    else:
        raise HTTPException(
            status_code=404,
            detail="Headlines Souurce not found"
        )

app = FastAPI()

@app.get("/headlines")
async def getHeadliines(headlines:list = Depends(updatedHeadlines)):
     return {
         "source":url,
         "headlines":headlines
     }

