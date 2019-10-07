from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

keyword = input("Search somthing: ")

browser = webdriver.Firefox(
    executable_path="geckodriver.exe")
browser.get("https://images.google.com/")

search = browser.find_element_by_name("q")
search.send_keys("{}".format(keyword), Keys.ENTER)

value = 0
for i in range(3):
    browser.execute_script("scrollBy(" + str(value) + ",+1000);")
    value += 1000
    time.sleep(3)

elem1 = browser.find_element_by_id("rg_s")

sub = elem1.find_elements_by_tag_name("img")

try:
    os.mkdir("downloads-{}".format(keyword))
except FileExistsError:
    pass

count = 0
for i in sub:
    src = i.get_attribute("src")
    try:
        if src != None:
            src = str(src)
            print(src)
            count += 1
            urllib.request.urlretrieve(src, os.path.join(
                "downloads-{}".format(keyword), "image" + str(count) + ".jpg"))
        else:
            raise TypeError
    except TypeError:
        print("fail")
