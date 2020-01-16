import requests
from bs4 import BeautifulSoup


def rule34(keywords, index):

    keywords = [f"{keyword}*" for keyword in keywords]
    keyword = "+".join(keywords)

    BASEURL = "https://rule34.xxx/"
    SEARCHURL = f"{BASEURL}index.php?page=post&s=list&tags={keyword}"

    soup = BeautifulSoup(requests.get(SEARCHURL).content, "html.parser")
    item = soup.find_all("span", class_="thumb")[index + 4]

    IMAGEURL = BASEURL + item.find("a")["href"]

    i_soup = BeautifulSoup(requests.get(IMAGEURL).content, "html.parser")
    image = i_soup.find_all("img", id="image")[0]

    return IMAGEURL, image["alt"], image["src"]
