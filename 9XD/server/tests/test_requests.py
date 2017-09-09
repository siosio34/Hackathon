import requests
from bs4 import BeautifulSoup
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_page():

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path=os.path.abspath("../driver/chromedriver_mac"), chrome_options=chrome_options)

    place_id = 653245473
    url = "http://place.map.daum.net/{}".format(place_id)

    while True:
        driver.get(url)
        html = driver.page_source
        if "상세정보" in html:
            break
    driver.close()

    soup = BeautifulSoup(html, "html.parser")
    result = soup.select("div.details_placeinfo")
    return html, result

def get_info():
    html, result = get_page()
    tag = result[0]
    info = {
        "address": None,
        "time": None,
        "contact": None,
    }

    info["address"] = "".join(line.strip() for line in tag.select("span.txt_address")[0].text.split("\n"))
    info["time"] = "".join(line.strip() for line in tag.select("span.txt_operation")[0].text.split("\n"))
    info["contact"] = "".join(line.strip() for line in tag.select("span.txt_contact")[0].text.split("\n"))


    return info
import time
a = time.time()
print(get_info())
b = time.time()
print("time : %.4f" % (b - a))
