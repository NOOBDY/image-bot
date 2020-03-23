import requests
from bs4 import BeautifulSoup
import os


def image(keywords, is_nsfw, index):
    keyword = "+".join(keywords)

    BASEURL = 'https://www.googleapis.com/customsearch/v1?'
    APIKEY = os.environ["APIKEY"]
    CX = "013191322677682374929:qdynn3gz9ku"
    SEARCHURL = f"{BASEURL}key={APIKEY}&cx={CX}&q={keyword}&safe={is_nsfw}&searchType=image"

    response = requests.get(SEARCHURL).json()
    items = response["items"]

    if len(items) == 0:
        return None
    elif len(items) < 10:
        index = round(((len(items) - 1) / 9) * (index - 1))
    else:
        index -= 1

    return items[index]["link"]
