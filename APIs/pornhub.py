import requests
from bs4 import BeautifulSoup


def pornhub(keywords: list[str], index: int):

    keyword = "+".join(keywords)
    r_keyword = keyword.replace("+", " ")

    BASEURL = "https://pornhub.com"
    SEARCHURL = f"{BASEURL}/video/search?search={keyword}"

    soup = BeautifulSoup(requests.get(SEARCHURL).content, "html.parser")
    items = soup.find_all("a", class_="linkVideoThumb")[5:]

    if len(items) == 0:
        return None, None, None, None
    elif len(items) < 10:
        index = round(((len(items) - 1) / 9) * index)
    item = items[index]

    return r_keyword, item["title"], f"{BASEURL}{item['href']}", item.img['data-src']


if __name__ == "__main__":
    print(pornhub(["what"], 0))
