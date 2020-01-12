import requests
from bs4 import BeautifulSoup


def pornhub(keywords, limit=10):

    # keyword is for the url, r_keyword is for displaying on the message
    keyword = "+".join(keywords)
    r_keyword = keyword.replace("+", " ")
    BASE_URL = "https://pornhub.com"
    SEARCH_URL = f"{BASE_URL}/video/search?search={keyword}"

    # initializing arrays
    titles = []
    urls = []
    thumbs = []

    # fetching data
    response = requests.get(SEARCH_URL)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    as_ = soup.find_all("a", class_="linkVideoThumb")

    # adding all found data into arrays
    for a in as_[4:]:
        if r_keyword in a['title'].lower():
            titles.append(a['title'])
            urls.append(f"{BASE_URL}{a['href']}")
            thumbs.append(a.img['data-src'])

    # return most relevant results, if any
    if len(urls) > 10:
        return r_keyword, titles[:10], urls[:10], thumbs[:10]
    elif len(urls) > 0:
        return r_keyword, titles, urls, thumbs
    else:
        return None, None, None, None


# unrelated code, testing purposes
if __name__ == "__main__":
    from random import randint
    search = input("Search something: ")
    keyword, titles, urls, thumbs = pornhub([search])
    if urls is not None:
        print(f"{len(titles)} result(s) found")
        for i in range(len(titles)):
            print(i + 1)
            print(titles[i])
            print(urls[i])
            print(thumbs[i])
            print()
    else:
        print("No results")
