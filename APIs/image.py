import requests
from bs4 import BeautifulSoup

def image(keywords, limits=10):
    keyword = "+".join(keywords)
    r_keyword = keyword.replace("+", " ")
    BASE_URL = "https://www.google.com"
    SEARCH_URL = f"tbm=isch&q={keyword}"