import requests
from bs4 import BeautifulSoup

def get_ranking_results(place_name):
    url = "http://www.diningcode.com/list.php?query={}%20카페".format(place_name)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    rank_10 = soup.select("#search_list > dc-restaurant")
    result_list = []

    for rank in rank_10:
        photos = rank.select("div.dc-restaurant-photo-container")[0]
        first_photo_url = photos.find("dc-rimage")["data-image"].split(",")[0]

        contents = rank.select("dc-restaurant-contents")[0]
        main_content = [line.strip() for line in contents.text.split()[:3]]
        cafe_name = main_content[0]
        keywords = main_content[1:3]

        info = rank.select("dc-restaurant-info")[0]
        main_info = [line for line in info.text.split("\n") if line is not ""]
        features = main_info[0]
        address = main_info[1]
        call_number = main_info[2]

        body = {
            "photo_url": first_photo_url,
            "cafe_name": cafe_name,
            "keywords": keywords,
            "features": features,
            "address": address,
            "call_number": call_number,
        }
        result_list.append(body)
    return {"rankingList": result_list}
