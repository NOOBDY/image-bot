import requests
from bs4 import BeautifulSoup


def rule34(keywords, index) -> dict[str, str]:
    """
    searches things on https://rule34.xxx
    returns a dictionary based on search results\n
    dictionary shape:\n
    ```
    {
        "url": url_to_page,
        "img": image_link
    }
    ```
    returns None if there's no search results
    """
    keyword = "_".join(keywords)

    BASEURL = "https://rule34.xxx/"
    SEARCHURL = f"{BASEURL}index.php?page=post&s=list&tags={keyword}*"

    soup = BeautifulSoup(requests.get(SEARCHURL).content, "html.parser")
    items = soup.find_all("span", class_="thumb")

    # scales the random index if the the result count is lesser than 10
    if len(items) == 0:
        return None
    elif len(items) < 10:
        index = round(((len(items) - 1) / 9) * index)
    item = items[index]

    IMAGEURL = BASEURL + item.find("a")["href"]

    i_soup = BeautifulSoup(requests.get(IMAGEURL).content, "html.parser")
    image = i_soup.find_all("img", id="image")[0]

    return {
        "url": IMAGEURL,
        "img": image["src"]
    }
