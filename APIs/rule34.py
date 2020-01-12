import requests
from bs4 import BeautifulSoup


def autocomplete(keyword):
    pass


def rule34(keywords):

    keyword = "+".join(keywords)
    BASEURL = "https://rule34.xxx/"
    AUTOCOMPLETEURL = f"{BASEURL}index.php?page=tags&s=list&tags={keyword}*&sort=desc&order_by=index_count"

    a_response = requests.get(AUTOCOMPLETEURL)
    a_html = a_response.content
    a_soup = BeautifulSoup(a_html, "html.parser")
    a_item = a_soup.find("span", class_="tag-type-general").findChild().text
    print(a_item)
    SEARCHURL = f"{BASEURL}{a_item}"
    print(SEARCHURL)


rule34(["loli"])
