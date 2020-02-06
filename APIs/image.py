<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

def image(keywords, limits=10):
    keyword = "+".join(keywords)
    r_keyword = keyword.replace("+", " ")
    BASE_URL = "https://www.google.com"
    SEARCH_URL = f"tbm=isch&q={keyword}"
=======
from google_images_download import google_images_download


def image(keywords, limit=10):

    response = google_images_download.googleimagesdownload()
    keyword = " ".join(keywords)
    args = {
        "keywords": keyword,
        "limit": limit,
        "print_urls": False,
        "no_download": True,
        "format": "jpg"
    }
    i = 0
    while i < 2:
        urls = []
        paths, errors = response.download(args)
        for path in paths[keyword]:
            urls.append(path)
        if len(urls) != 0:
            return keyword.replace(",", " "), urls
        else:
            i += 1
    return None
>>>>>>> master
