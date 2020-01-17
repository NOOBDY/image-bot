import requests
from bs4 import BeautifulSoup
from random import randint


def rule34(keywords, index):

    keywords = [f"{keyword}*" for keyword in keywords]
    keyword = "+".join(keywords)

    BASEURL = "https://rule34.xxx/"
    SEARCHURL = f"{BASEURL}index.php?page=post&s=list&tags={keyword}"

    soup = BeautifulSoup(requests.get(SEARCHURL).content, "html.parser")
    items = soup.find_all("span", class_="thumb")
    # scales the random index if the the result count is lesser than 10
    if len(items) == 0:
        return None, None, None
    elif len(items) < 10:
        index = round(((len(items) - 1) / 9) * (index - 1))
    else:
        index -= 1
    item = items[index]

    IMAGEURL = BASEURL + item.find("a")["href"]

    i_soup = BeautifulSoup(requests.get(IMAGEURL).content, "html.parser")
    image = i_soup.find_all("img", id="image")[0]

    return IMAGEURL, image["alt"], image["src"]


for i in range(1, 11):
    index = i
    print(index)
    print(rule34(["as"], index))
