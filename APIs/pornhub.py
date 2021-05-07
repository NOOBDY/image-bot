import requests
from bs4 import BeautifulSoup


def pornhub(keywords: list[str], index: int) -> dict[str, str]:
    """
    searches videos on https://www.pornhub.com
    returns a dictionary based on search results\n
    dictionary shape:\n
    ```
    {
        "title": title,
        "url": url,
        "thumbnail": thumbnail_image_link
    }
    ```
    returns None if there's no search results
    """

    keyword = "+".join(keywords)

    BASEURL = "https://www.pornhub.com"
    SEARCHURL = f"{BASEURL}/video/search?search={keyword}"

    soup = BeautifulSoup(requests.get(SEARCHURL).content, "html.parser")
    items = soup.find_all("a", class_="linkVideoThumb")[5:]

    if len(items) == 0:
        return None
    elif len(items) < 10:
        index = round(((len(items) - 1) / 9) * index)
    item = items[index]

    return {
        "title": item["title"],
        "url": f"{BASEURL}{item['href']}",
        "thumbnail": item.img['data-src']
    }
