import requests
from bs4 import BeautifulSoup

def pornhub(keywords, limit=10):

    keyword = "+".join(keywords)
    BASE_URL = "https://pornhub.com"
    SEARCH_URL = f"{BASE_URL}/video/search?search={keyword}"
    
    response = requests.get(SEARCH_URL)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    as_ = soup.find_all("a", class_="linkVideoThumb")

    titles = []
    urls = []
    thumbs = []

    for a in as_[4:]:
        titles.append(a['title'])
        urls.append(f"{BASE_URL}{a['href']}")
        thumbs.append(a.img['data-src'])
    
    r_keyword = keyword.replace("+", " ")
    
    if len(urls) > 10:
        return r_keyword, titles[:10], urls[:10], thumbs[:10]
    else:
        return r_keyword, titles, urls, thumbs

if __name__ == "__main__":
    from random import randint
    keyword, titles, urls, thumbs = pornhub(["ableton"]);
    i = randint(0, len(titles) - 1)
    print(i)
    print(len(titles))
    print(titles[i])
    print(urls[i])
    print(thumbs[i])
    print()